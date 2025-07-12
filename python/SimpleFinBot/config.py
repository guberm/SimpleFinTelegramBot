"""
Configuration module for SimpleFIN Telegram Bot Python version.
"""

import json
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class TelegramBotConfig:
    """Telegram Bot configuration."""
    bot_token: str = ""
    webapp_url: str = "https://your-webapp-domain.com/index.html"


@dataclass
class DatabaseConfig:
    """Database configuration."""
    connection_string: str = "Data Source=simplefin_multi_accounts.db"


@dataclass
class BotConfig:
    """Main bot configuration."""
    telegram_bot: TelegramBotConfig
    database: DatabaseConfig
    
    @classmethod
    def load_config(cls) -> 'BotConfig':
        """Load configuration from environment variables and config file."""
        # Try to load from config.json first
        config_data = {}
        
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                config_data = json.load(f)
        except FileNotFoundError:
            # Create default config file if it doesn't exist
            default_config = {
                "telegram_bot": {
                    "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
                    "webapp_url": "https://your-webapp-domain.com/index.html"
                },
                "database": {
                    "connection_string": "Data Source=simplefin_multi_accounts.db"
                }
            }
            
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(default_config, f, indent=2)
            
            config_data = default_config
        
        # Override with environment variables if available
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN") or config_data.get("telegram_bot", {}).get("bot_token", "")
        webapp_url = os.getenv("TELEGRAM_WEBAPP_URL") or config_data.get("telegram_bot", {}).get("webapp_url", "https://your-webapp-domain.com/index.html")
        connection_string = os.getenv("DATABASE_CONNECTION_STRING") or config_data.get("database", {}).get("connection_string", "Data Source=simplefin_multi_accounts.db")
        
        telegram_config = TelegramBotConfig(
            bot_token=bot_token,
            webapp_url=webapp_url
        )
        
        database_config = DatabaseConfig(
            connection_string=connection_string
        )
        
        return cls(
            telegram_bot=telegram_config,
            database=database_config
        )
