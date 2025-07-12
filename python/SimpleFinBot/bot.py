#!/usr/bin/env python3
"""
SimpleFIN Telegram Bot - Python Version

A comprehensive Telegram Bot solution for managing SimpleFIN financial accounts integration.
Built with Python, sqlite3, and python-telegram-bot.
"""

import asyncio
import base64
import json
import logging
import os
import sqlite3
import sys
from datetime import datetime
from typing import List, Optional, Tuple
from urllib.parse import urlparse

import aiohttp
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    WebAppInfo,
)
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from config import BotConfig

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class SimpleFinBot:
    """SimpleFIN Telegram Bot main class."""
    
    def __init__(self, config: BotConfig):
        """Initialize the bot with configuration."""
        self.config = config
        self.db_path = config.database.connection_string.replace("Data Source=", "")
        self._init_database()
    
    def _init_database(self) -> None:
        """Initialize SQLite database with required tables."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS accounts (
                        user_id INTEGER,
                        access_url TEXT,
                        bank_name TEXT,
                        created_at TEXT,
                        PRIMARY KEY (user_id, access_url)
                    )
                """)
                conn.commit()
            logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /start and /help commands."""
        help_text = (
            "Welcome!\n\n"
            "/add — Add a new bank\n"
            "/accounts — List your banks and accounts\n"
            "/remove — Remove a bank\n"
            "/refresh — Refresh accounts\n"
            "/web — Open WebApp\n"
            "To add a bank, use /add."
        )
        await update.message.reply_text(help_text)
    
    async def add_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /add command."""
        text = (
            "To add a bank, follow the link:\n"
            "https://bridge.simplefin.org/simplefin/create\n"
            "Copy the token and send it to me."
        )
        await update.message.reply_text(text)
    
    async def accounts_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /accounts and /refresh commands."""
        user_id = update.effective_user.id
        banks = self._get_banks(user_id)
        
        if not banks:
            await update.message.reply_text(
                "You have no connected banks. Use /add to connect one."
            )
            return
        
        response_parts = ["Your connected banks:\n"]
        
        for access_url, bank_name in banks:
            accounts_data = await self._get_simplefin_accounts(access_url)
            response_parts.append(f"\n<b>{bank_name}</b>")
            
            if accounts_data and "accounts" in accounts_data and accounts_data["accounts"]:
                for account in accounts_data["accounts"]:
                    name = account.get("name", "Unknown")
                    balance = account.get("balance", "0")
                    currency = account.get("currency", "USD")
                    account_id = account.get("id", "")
                    response_parts.append(
                        f"    Account: <b>{name}</b> ({currency}), "
                        f"Balance: <b>{balance}</b>, ID: <code>{account_id}</code>"
                    )
            else:
                response_parts.append("    Unable to retrieve data.")
        
        await update.message.reply_text(
            "\n".join(response_parts), parse_mode=ParseMode.HTML
        )
    
    async def remove_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /remove command."""
        user_id = update.effective_user.id
        banks = self._get_banks(user_id)
        
        if not banks:
            await update.message.reply_text("You have no connected banks.")
            return
        
        keyboard = [
            [KeyboardButton(f"{i + 1}. {bank_name}")]
            for i, (_, bank_name) in enumerate(banks)
        ]
        
        reply_markup = ReplyKeyboardMarkup(
            keyboard, one_time_keyboard=True, resize_keyboard=True
        )
        
        await update.message.reply_text(
            "Select the bank to remove (send the number):",
            reply_markup=reply_markup
        )
    
    async def web_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /web command."""
        web_app_url = self.config.telegram_bot.webapp_url
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "Open WebApp", 
                web_app=WebAppInfo(url=web_app_url)
            )]
        ])
        
        await update.message.reply_text(
            "Click the button to open your SimpleFIN dashboard:",
            reply_markup=markup
        )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle text messages (tokens and bank removal numbers)."""
        message_text = update.message.text
        user_id = update.effective_user.id
        
        # Handle SimpleFIN token
        if len(message_text) > 40 and "=" in message_text:
            await update.message.reply_text("Connecting...")
            
            access_url = await self._claim_access_url(message_text)
            if not access_url:
                await update.message.reply_text("❌ Invalid or used token.")
                return
            
            accounts_data = await self._get_simplefin_accounts(access_url)
            bank_name = self._get_bank_name_from_data(accounts_data) or "Bank"
            
            self._add_bank(user_id, access_url, bank_name)
            await update.message.reply_text(f"✅ Bank '{bank_name}' has been connected!")
        
        # Handle bank removal by number
        elif message_text.split('.')[0].isdigit():
            try:
                bank_index = int(message_text.split('.')[0]) - 1
                banks = self._get_banks(user_id)
                
                if not banks or bank_index < 0 or bank_index >= len(banks):
                    await update.message.reply_text("Invalid number.")
                    return
                
                access_url = banks[bank_index][0]
                self._remove_bank(user_id, access_url)
                
                await update.message.reply_text(
                    "Bank connection removed.",
                    reply_markup=ReplyKeyboardRemove()
                )
            except (ValueError, IndexError):
                await update.message.reply_text("Invalid number.")
    
    def _add_bank(self, user_id: int, access_url: str, bank_name: str) -> None:
        """Add a bank connection to the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO accounts (user_id, access_url, bank_name, created_at) VALUES (?, ?, ?, ?)",
                (user_id, access_url, bank_name, datetime.utcnow().isoformat())
            )
            conn.commit()
    
    def _remove_bank(self, user_id: int, access_url: str) -> None:
        """Remove a bank connection from the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM accounts WHERE user_id = ? AND access_url = ?",
                (user_id, access_url)
            )
            conn.commit()
    
    def _get_banks(self, user_id: int) -> List[Tuple[str, str]]:
        """Get all bank connections for a user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT access_url, bank_name FROM accounts WHERE user_id = ?",
                (user_id,)
            )
            return cursor.fetchall()
    
    def _get_bank_name_from_data(self, data: Optional[dict]) -> Optional[str]:
        """Extract bank name from SimpleFIN account data."""
        if not data or "accounts" not in data or not data["accounts"]:
            return None
        
        try:
            org = data["accounts"][0].get("org", {})
            return org.get("domain") or org.get("name")
        except (KeyError, IndexError):
            return None
    
    async def _claim_access_url(self, setup_token: str) -> Optional[str]:
        """Claim access URL from SimpleFIN setup token."""
        try:
            decoded_bytes = base64.b64decode(setup_token)
            url = decoded_bytes.decode('utf-8')
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url) as response:
                    if response.status == 200:
                        return (await response.text()).strip()
        except Exception as e:
            logger.error(f"Failed to claim access URL: {e}")
        
        return None
    
    async def _get_simplefin_accounts(self, access_url: str) -> Optional[dict]:
        """Get account data from SimpleFIN API."""
        try:
            parsed_url = urlparse(access_url + "/accounts")
            username, password = parsed_url.username, parsed_url.password
            
            base_url = f"{parsed_url.scheme}://{parsed_url.hostname}"
            if parsed_url.port:
                base_url += f":{parsed_url.port}"
            base_url += f"{parsed_url.path}/accounts"
            
            auth = aiohttp.BasicAuth(username, password)
            
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url, auth=auth) as response:
                    if response.status == 200:
                        return await response.json()
        except Exception as e:
            logger.error(f"Failed to get SimpleFIN accounts: {e}")
        
        return None
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle errors."""
        logger.error(f"Exception while handling an update: {context.error}")


async def main():
    """Main function to run the bot."""
    # Load configuration
    config = BotConfig.load_config()
    
    # Validate bot token
    if not config.telegram_bot.bot_token or config.telegram_bot.bot_token in [
        "YOUR_TELEGRAM_BOT_TOKEN", 
        "YOUR_DEVELOPMENT_BOT_TOKEN"
    ]:
        print("ERROR: Please configure a valid Telegram bot token")
        print("You can get a bot token from @BotFather on Telegram")
        print("Update the bot token in config.json or set the TELEGRAM_BOT_TOKEN environment variable")
        sys.exit(1)
    
    # Create bot instance
    bot = SimpleFinBot(config)
    
    # Create application
    application = Application.builder().token(config.telegram_bot.bot_token).build()
    
    # Add handlers
    application.add_handler(CommandHandler(["start", "help"], bot.start_command))
    application.add_handler(CommandHandler("add", bot.add_command))
    application.add_handler(CommandHandler(["accounts", "refresh"], bot.accounts_command))
    application.add_handler(CommandHandler("remove", bot.remove_command))
    application.add_handler(CommandHandler("web", bot.web_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    
    # Add error handler
    application.add_error_handler(bot.error_handler)
    
    # Start the bot
    print("Bot started. Press Ctrl+C to stop.")
    await application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    asyncio.run(main())
