# Python Bot Configuration Guide

## 🐍 Setting Up Your Python SimpleFIN Telegram Bot

### Method 1: JSON Configuration File (Recommended for Development)

The bot will automatically create a `config.json` file when you first run it. Edit this file with your actual bot token:

```json
{
  "telegram_bot": {
    "bot_token": "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi",
    "webapp_url": "https://your-webapp-domain.com/index.html"
  },
  "database": {
    "connection_string": "Data Source=simplefin_multi_accounts.db"
  }
}
```

### Method 2: Environment Variables (Recommended for Production)

Set these environment variables:

#### Windows (PowerShell):
```powershell
$env:TELEGRAM_BOT_TOKEN="your_bot_token_here"
$env:TELEGRAM_WEBAPP_URL="https://your-webapp-domain.com/index.html"
$env:DATABASE_CONNECTION_STRING="Data Source=simplefin_multi_accounts.db"
```

#### Windows (Command Prompt):
```cmd
set TELEGRAM_BOT_TOKEN=your_bot_token_here
set TELEGRAM_WEBAPP_URL=https://your-webapp-domain.com/index.html
set DATABASE_CONNECTION_STRING=Data Source=simplefin_multi_accounts.db
```

#### Linux/macOS:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_WEBAPP_URL="https://your-webapp-domain.com/index.html"
export DATABASE_CONNECTION_STRING="Data Source=simplefin_multi_accounts.db"
```

### Getting a Bot Token

1. Open Telegram and search for `@BotFather`
2. Start a conversation and send `/newbot`
3. Follow the instructions to create your bot
4. Copy the bot token provided by BotFather

### Configuration Priority

The Python bot checks for configuration in this order:
1. **Environment variables** (highest priority)
2. **config.json file** (lowest priority)

### Quick Start Commands

1. **Install dependencies:**
   ```bash
   cd python/SimpleFinBot
   pip install -r requirements.txt
   ```

2. **Configure your bot token** (choose one method above)

3. **Run the bot:**
   ```bash
   python bot.py
   ```

4. **In another terminal, start the API:**
   ```bash
   cd python/SimpleFinWebApi
   pip install -r requirements.txt
   python api.py
   ```

### Security Notes

- ✅ Never commit real bot tokens to version control
- ✅ Use environment variables for production deployments
- ✅ The config.json file should be added to `.gitignore`
- ✅ Placeholder tokens will cause the bot to exit with an error message
- ✅ Both config file and environment variables are validated on startup

### Troubleshooting

#### Bot won't start:
- Check that your bot token is valid
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.8 or higher: `python --version`

#### API connection issues:
- Make sure the API is running on port 8000
- Check firewall settings
- Verify the database file is accessible

#### WebApp not working:
- Update the webapp_url in your configuration
- Ensure the WebApp HTML file is hosted and accessible
- Check that the API URL in the HTML file matches your API server
