# SimpleFIN Telegram Bot - C# Version

A comprehensive .NET 8 implementation of the SimpleFIN Telegram Bot with ASP.NET Core backend and Telegram WebApp interface.

## 🚀 Features

- **🤖 Telegram Bot**: Full-featured console application with advanced configuration
- **🌐 ASP.NET Core API**: High-performance REST API with CORS support
- **📱 WebApp Interface**: HTML5 interface for Telegram WebApp
- **⚙️ Advanced Configuration**: appsettings.json + environment variables
- **🔒 Security**: Built-in validation and secure database operations
- **🛠️ VS Code Integration**: Complete development environment setup

## 🛠️ Requirements

- .NET 8 SDK
- Visual Studio Code (recommended) or Visual Studio

## 📦 Installation

### 1. Restore Dependencies
```bash
dotnet restore
```

### 2. Configuration

#### Method 1: Configuration Files (Development)
Edit `SimpleFinBot/appsettings.Development.json`:
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

For detailed configuration instructions, see [BOT_CONFIGURATION.md](SimpleFinBot/BOT_CONFIGURATION.md).

## 🚀 Running the Application

### Option 1: Using VS Code Tasks
1. Open in VS Code
2. Use `Ctrl+Shift+P` → "Tasks: Run Task"
3. Select "Run Web API" and "Run Telegram Bot"

### Option 2: Manual Commands

#### Start the Web API:
```bash
dotnet run --project SimpleFinWebApi
```
The API will be available at `http://localhost:5171`

#### Start the Telegram Bot:
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

## 🏗️ Project Structure

```
csharp/
├── SimpleFinBot/              # Telegram Bot (Console App)
│   ├── Program.cs             # Main bot logic
│   ├── appsettings.json       # Configuration file
│   ├── appsettings.Development.json
│   ├── Configuration/
│   │   └── BotSettings.cs     # Configuration models
│   └── BOT_CONFIGURATION.md   # Setup instructions
├── SimpleFinWebApi/           # ASP.NET Core Web API
│   ├── Controllers/
│   │   └── AccountsController.cs
│   └── Program.cs
├── SimpleFinWebApp/           # Static WebApp
│   └── index.html
├── SimpleFinTelegram.sln      # Solution file
└── .github/
    └── workflows/
        └── dotnet.yml         # CI/CD pipeline
```

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

## 🚀 Production Deployment

### Using Docker:
```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["SimpleFinWebApi/SimpleFinWebApi.csproj", "SimpleFinWebApi/"]
RUN dotnet restore "SimpleFinWebApi/SimpleFinWebApi.csproj"
COPY . .
WORKDIR "/src/SimpleFinWebApi"
RUN dotnet build "SimpleFinWebApi.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SimpleFinWebApi.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SimpleFinWebApi.dll"]
```

### CI/CD with GitHub Actions:
The project includes a complete GitHub Actions workflow in `.github/workflows/dotnet.yml` for:
- Automatic building on push/PR
- .NET 8 compatibility testing
- Dependency restoration
- Build verification

## 📄 License

This project is a template for SimpleFIN integration with Telegram bots.
