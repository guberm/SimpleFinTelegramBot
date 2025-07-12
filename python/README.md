# SimpleFIN Telegram Bot - Python Version

A comprehensive Python implementation of the SimpleFIN Telegram Bot with FastAPI backend and modern WebApp interface.

## 🚀 Features

- **🤖 Telegram Bot**: Full-featured bot with async/await support
- **🌐 FastAPI Backend**: High-performance REST API with automatic documentation
- **📱 Modern WebApp**: Enhanced HTML5 interface with Telegram theming
- **⚙️ Flexible Configuration**: JSON config files + environment variables
- **🔒 Security**: Built-in validation and secure database operations
- **📊 Type Safety**: Full type hints and Pydantic models

## 🛠️ Requirements

- Python 3.8+
- pip (Python package manager)

## 📦 Installation

### 1. Install Dependencies

#### Bot Dependencies:
```bash
cd python/SimpleFinBot
pip install -r requirements.txt
```

#### API Dependencies:
```bash
cd python/SimpleFinWebApi
pip install -r requirements.txt
```

### 2. Configuration

#### Method 1: Config File (Recommended for Development)
The bot will automatically create a `config.json` file on first run. Edit it with your bot token:

```json
{
  "telegram_bot": {
    "bot_token": "YOUR_ACTUAL_BOT_TOKEN_HERE",
    "webapp_url": "https://your-webapp-domain.com/index.html"
  },
  "database": {
    "connection_string": "Data Source=simplefin_multi_accounts.db"
  }
}
```

#### Method 2: Environment Variables (Recommended for Production)
```bash
# Windows PowerShell
$env:TELEGRAM_BOT_TOKEN="your_bot_token_here"
$env:TELEGRAM_WEBAPP_URL="https://your-webapp-domain.com/index.html"

# Linux/macOS
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_WEBAPP_URL="https://your-webapp-domain.com/index.html"
```

## 🚀 Running the Application

### Start the API Server:
```bash
cd python/SimpleFinWebApi
python api.py
```
The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### Start the Telegram Bot:
```bash
cd python/SimpleFinBot
python bot.py
```

## 📋 Usage

1. Start a chat with your Telegram bot
2. Use `/add` to get SimpleFIN setup instructions
3. Follow the SimpleFIN bridge link to generate a token
4. Send the token to the bot to connect your bank
5. Use `/accounts` to view your connected accounts
6. Use `/web` to open the WebApp interface

## 🔧 Development

### Project Structure:
```
python/
├── SimpleFinBot/          # Telegram Bot
│   ├── bot.py            # Main bot application
│   ├── config.py         # Configuration management
│   └── requirements.txt  # Bot dependencies
├── SimpleFinWebApi/       # FastAPI Backend
│   ├── api.py            # Main API application
│   └── requirements.txt  # API dependencies
└── SimpleFinWebApp/       # WebApp Frontend
    └── index.html        # Enhanced web interface
```

### Key Features:

#### Bot (bot.py):
- Async/await support for better performance
- Type hints for better code quality
- Comprehensive error handling
- Structured logging
- Configuration validation

#### API (api.py):
- FastAPI with automatic OpenAPI documentation
- Pydantic models for request/response validation
- CORS middleware for cross-origin requests
- Health check endpoints
- Structured error responses

#### WebApp (index.html):
- Telegram WebApp theming support
- Enhanced UI with loading states
- Error handling and user feedback
- Responsive design
- Version identification

## 🔒 Security Features

- Environment variable support for sensitive data
- Input validation and sanitization
- Parameterized database queries
- CORS configuration
- Token validation with helpful error messages

## 📚 API Documentation

When the API is running, visit `http://localhost:8000/docs` for interactive API documentation powered by FastAPI's automatic OpenAPI generation.

### Available Endpoints:

- `GET /api/accounts?user_id={id}` - Get user's bank accounts
- `GET /health` - Health check
- `GET /` - API information

## 🧪 Testing

### Test the API:
```bash
# Health check
curl http://localhost:8000/health

# Get accounts (replace USER_ID with actual Telegram user ID)
curl "http://localhost:8000/api/accounts?user_id=USER_ID"
```

### Test the Bot:
1. Start the bot
2. Send `/start` to your bot
3. Verify all commands work correctly

## 🔄 Comparison with C# Version

| Feature | C# Version | Python Version |
|---------|------------|----------------|
| **Framework** | .NET 8 Console App | Python asyncio |
| **API** | ASP.NET Core | FastAPI |
| **Database** | SQLite with Microsoft.Data.Sqlite | SQLite with built-in sqlite3 |
| **Configuration** | appsettings.json + Environment Variables | JSON config + Environment Variables |
| **Documentation** | XML docs | Type hints + docstrings |
| **Performance** | High (compiled) | High (async/await) |
| **Deployment** | Single executable | Python runtime required |

## 🚀 Production Deployment

### Using Docker (Recommended):
Create a `Dockerfile` for each component:

```dockerfile
# Bot Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

### Using systemd (Linux):
Create service files for automatic startup and monitoring.

## 📄 License

This project is a template for SimpleFIN integration with Telegram bots.
