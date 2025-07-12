# SimpleFinBot Configuration

## Setting Up Your Telegram Bot Token

### Method 1: Using Configuration Files (Recommended for Development)

1. Open `appsettings.json` or `appsettings.Development.json`
2. Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual bot token:

```json
{
  "TelegramBot": {
    "BotToken": "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"
  }
}
```

### Method 2: Using Environment Variables (Recommended for Production)

Set the environment variable:
- **Windows (PowerShell)**: `$env:TELEGRAMBOT__BOTTOKEN="your_bot_token_here"`
- **Windows (CMD)**: `set TELEGRAMBOT__BOTTOKEN=your_bot_token_here`
- **Linux/macOS**: `export TELEGRAMBOT__BOTTOKEN="your_bot_token_here"`

### Getting a Bot Token

1. Open Telegram and search for `@BotFather`
2. Start a conversation and send `/newbot`
3. Follow the instructions to create your bot
4. Copy the bot token provided by BotFather

### Configuration Priority

The bot will check for the token in this order:
1. Environment variables (highest priority)
2. appsettings.{Environment}.json (e.g., appsettings.Development.json)
3. appsettings.json (lowest priority)

### Security Notes

- Never commit real bot tokens to version control
- Add `appsettings.*.json` files with real tokens to `.gitignore`
- Use environment variables for production deployments
- The placeholder tokens (`YOUR_TELEGRAM_BOT_TOKEN`, `YOUR_DEVELOPMENT_BOT_TOKEN`) will cause the bot to exit with an error message
