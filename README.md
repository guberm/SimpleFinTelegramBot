# SimpleFIN Telegram Bot

> 🏦 **Complete Financial Integration Solution** - A full-stack C# ecosystem combining Telegram Bot, Web API, and WebApp for seamless banking data access through SimpleFIN integration.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![.NET](https://img.shields.io/badge/.NET-9.0-512BD4)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4)]()

A comprehensive Telegram Bot + Web API solution for managing SimpleFIN financial accounts integration, built with C# and SQLite. This project enables users to securely connect their bank accounts and access financial information through both conversational bot commands and a modern web interface.

## Project Structure

```
SimpleFinTelegram/
├─ SimpleFinBot/              # Telegram Bot (Console App)
│  └─ Program.cs
├─ SimpleFinWebApi/           # ASP.NET Core Web API (WebApp backend)
│  ├─ Controllers/
│  │   └─ AccountsController.cs
│  └─ Program.cs
├─ SimpleFinWebApp/           # Static folder for frontend
│  └─ index.html
└─ SimpleFinTelegram.sln
```

## Features

### Telegram Bot Commands
- `/start` and `/help` - Show available commands
- `/add` - Add a new bank connection via SimpleFIN token
- `/accounts` and `/refresh` - List all connected banks and accounts
- `/remove` - Remove a bank connection
- `/web` - Open the WebApp interface

### Web API
- `GET /api/accounts?user_id={id}` - Retrieve banks for a specific user
- CORS enabled for cross-origin requests

### WebApp Frontend
- HTML interface for displaying connected banks
- Integration with Telegram WebApp API
- Direct link to SimpleFIN setup

## Setup Instructions

### Prerequisites
- .NET 8 SDK
- Telegram Bot Token (from @BotFather)

### Installation

1. **Clone and restore packages:**
   ```bash
   dotnet restore
   ```

2. **Configure Bot Token:**
   - Edit `SimpleFinBot/Program.cs`
   - Replace `"YOUR_TELEGRAM_BOT_TOKEN"` with your actual bot token

3. **Configure WebApp URL:**
   - Edit `SimpleFinBot/Program.cs`
   - Replace `"https://your-webapp-domain.com/index.html"` with your hosted WebApp URL
   - Edit `SimpleFinWebApp/index.html`
   - Replace `"http://localhost:5171"` with your API endpoint (if deploying to production)

### Running the Application

1. **Start the Web API:**
   ```bash
   dotnet run --project SimpleFinWebApi/SimpleFinWebApi.csproj
   ```
   The API will be available at `http://localhost:5171`

2. **Start the Telegram Bot (in a new terminal):**
   ```bash
   dotnet run --project SimpleFinBot/SimpleFinBot.csproj
   ```

3. **Host the WebApp:**
   - Deploy `SimpleFinWebApp/index.html` to your web server
   - Update the URL in the bot configuration

## Usage

1. Start a chat with your Telegram bot
2. Use `/add` to get SimpleFIN setup instructions
3. Follow the SimpleFIN bridge link to generate a token
4. Send the token to the bot to connect your bank
5. Use `/accounts` to view your connected accounts
6. Use `/web` to open the WebApp interface

## Database

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

## Security Notes

- Store bot tokens securely (environment variables recommended)
- Use HTTPS for production deployments
- Validate all user inputs
- Use parameterized database queries
- Handle SimpleFIN credentials securely

## Dependencies

### SimpleFinBot
- Telegram.Bot
- Microsoft.Data.Sqlite

### SimpleFinWebApi
- Microsoft.Data.Sqlite
- ASP.NET Core

## License

This project is a template for SimpleFIN integration with Telegram bots.
