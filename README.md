# SimpleFIN Telegram Bot

> 🏦 **Complete Financial Integration Solution** - A full-stack C# ecosystem combining Telegram Bot, Web API, and WebApp for seamless banking data access through SimpleFIN integration.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![.NET](https://img.shields.io/badge/.NET-8.0-512BD4)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4)]()

A comprehensive Telegram Bot + Web API solution for managing SimpleFIN financial accounts integration, built with C# and SQLite. This project enables users to securely connect their bank accounts and access financial information through both conversational bot commands and a modern web interface.

## 🚀 Features

### 🤖 Telegram Bot Commands
- `/start` and `/help` - Show available commands and guidance
- `/add` - Add a new bank connection via SimpleFIN token
- `/accounts` and `/refresh` - List all connected banks and accounts with real-time data
- `/remove` - Remove a bank connection securely
- `/web` - Open the integrated WebApp interface

### 🌐 Web API Endpoints
- `GET /api/accounts?user_id={id}` - Retrieve banks for a specific user
- CORS enabled for cross-origin requests
- RESTful design with proper error handling

### 📱 WebApp Frontend
- Modern HTML5 interface integrated with Telegram WebApp API
- Real-time account balance display
- Direct link to SimpleFIN setup
- Responsive design for mobile and desktop

### ⚙️ Configuration System
- **Secure Token Management**: Support for environment variables and configuration files
- **Multi-Environment**: Separate configurations for development and production
- **Validation**: Built-in token validation with helpful error messages
- **Easy Setup**: Clear documentation and examples

## 🏗️ Project Structure

```
SimpleFinTelegram/
├─ SimpleFinBot/              # Telegram Bot (Console App)
│  ├─ Program.cs              # Main bot logic
│  ├─ appsettings.json        # Configuration file
│  ├─ appsettings.Development.json
│  ├─ Configuration/
│  │   └─ BotSettings.cs      # Configuration models
│  └─ BOT_CONFIGURATION.md    # Setup instructions
├─ SimpleFinWebApi/           # ASP.NET Core Web API (WebApp backend)
│  ├─ Controllers/
│  │   └─ AccountsController.cs
│  └─ Program.cs
├─ SimpleFinWebApp/           # Static folder for frontend
│  └─ index.html
└─ SimpleFinTelegram.sln
```

## 🛠️ Setup Instructions

### Prerequisites
- .NET 8 SDK
- Telegram Bot Token (from @BotFather)

### 1. Clone and Restore
```bash
git clone https://github.com/guberm/SimpleFinTelegramBot.git
cd SimpleFinTelegramBot
dotnet restore
```

### 2. Configure Bot Token

#### Method 1: Configuration Files (Development)
1. Edit `SimpleFinBot/appsettings.Development.json`
2. Replace the bot token:
```json
{
  "TelegramBot": {
    "BotToken": "YOUR_ACTUAL_BOT_TOKEN_HERE"
  }
}
```

#### Method 2: Environment Variables (Production)
```bash
# Windows PowerShell
$env:TELEGRAMBOT__BOTTOKEN="your_bot_token_here"

# Linux/macOS
export TELEGRAMBOT__BOTTOKEN="your_bot_token_here"
```

### 3. Getting a Bot Token
1. Open Telegram and search for `@BotFather`
2. Start a conversation and send `/newbot`
3. Follow the instructions to create your bot
4. Copy the bot token provided by BotFather

For detailed configuration instructions, see [BOT_CONFIGURATION.md](SimpleFinBot/BOT_CONFIGURATION.md).

## 🚀 Running the Application

### Option 1: Using VS Code Tasks
1. Open in VS Code
2. Use `Ctrl+Shift+P` → "Tasks: Run Task"
3. Select "Run Web API" and "Run Telegram Bot"

### Option 2: Manual Commands

1. **Start the Web API:**
   ```bash
   dotnet run --project SimpleFinWebApi
   ```
   The API will be available at `http://localhost:5171`

2. **Start the Telegram Bot (in a new terminal):**
   ```bash
   dotnet run --project SimpleFinBot
   ```

## 📋 Usage

1. Start a chat with your Telegram bot
2. Use `/add` to get SimpleFIN setup instructions
3. Follow the SimpleFIN bridge link to generate a token
4. Send the token to the bot to connect your bank
5. Use `/accounts` to view your connected accounts
6. Use `/web` to open the WebApp interface

## 💾 Database

The application uses SQLite with the following schema:

```sql
accounts (
    user_id INTEGER,
    access_url TEXT,
    bank_name TEXT,
    created_at TEXT,
    PRIMARY KEY (user_id, access_url)
)
```

Database file: `simplefin_multi_accounts.db` (shared between Bot and API)

## 🔒 Security Features

- ✅ Environment variable support for sensitive data
- ✅ Token validation with helpful error messages  
- ✅ Parameterized database queries
- ✅ CORS configuration for API security
- ✅ SimpleFIN credential encryption
- ✅ Input validation and sanitization

## 📦 Dependencies

### SimpleFinBot
- `Telegram.Bot` (v19.0.0) - Telegram Bot API
- `Microsoft.Data.Sqlite` (v8.0.11) - Database access
- `Microsoft.Extensions.Configuration.*` - Configuration management

### SimpleFinWebApi
- `Microsoft.Data.Sqlite` (v8.0.11) - Database access
- `Microsoft.AspNetCore.OpenApi` (v8.0.11) - API documentation

## 🧪 Development

### Building
```bash
dotnet build
```

### Testing
```bash
dotnet test
```

### Clean Build
```bash
dotnet clean
dotnet restore
dotnet build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is a template for SimpleFIN integration with Telegram bots.

## 📞 Support

- Check [BOT_CONFIGURATION.md](SimpleFinBot/BOT_CONFIGURATION.md) for setup issues
- Review VS Code tasks for development workflow
- Check GitHub Issues for known problems
