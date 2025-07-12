# SimpleFIN Telegram Bot

> 🏦 **Complete Financial Integration Solution** - A comprehensive multi-language ecosystem with C# (.NET 8) and Python implementations for SimpleFIN banking integration through Telegram Bot, Web API, and WebApp interfaces.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![.NET](https://img.shields.io/badge/.NET-8.0-512BD4)]()
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4)]()

A dual-language implementation of SimpleFIN financial accounts integration with Telegram. Choose between C# (.NET 8) or Python implementations, both featuring secure configuration, real-time financial data access, and modern web interfaces.

## 🚀 Available Implementations

### 🔷 C# (.NET 8) Version
- **Enterprise-grade** .NET 8 console application and ASP.NET Core API
- **Advanced Configuration** with appsettings.json and environment variables
- **VS Code Integration** with complete development environment
- **GitHub Actions CI/CD** for automated building and testing

📂 **Location**: [`/csharp`](./csharp/) | 📖 **Documentation**: [C# README](./csharp/README.md)

### 🐍 Python Version  
- **Modern async/await** Python implementation with FastAPI
- **Type Safety** with full type hints and Pydantic models
- **Auto-Documentation** with FastAPI's OpenAPI integration
- **Flexible Deployment** options for containers and cloud platforms

📂 **Location**: [`/python`](./python/) | 📖 **Documentation**: [Python README](./python/README.md)

## 🎯 Choose Your Implementation

| Feature | C# (.NET 8) | Python |
|---------|-------------|---------|
| **Performance** | ⭐⭐⭐⭐⭐ Compiled, very fast | ⭐⭐⭐⭐ Fast with async/await |
| **Memory Usage** | ⭐⭐⭐⭐ Efficient | ⭐⭐⭐ Moderate |
| **Development Speed** | ⭐⭐⭐ Structured, enterprise | ⭐⭐⭐⭐⭐ Rapid prototyping |
| **Deployment** | ⭐⭐⭐⭐⭐ Single executable | ⭐⭐⭐ Runtime required |
| **Documentation** | ⭐⭐⭐⭐ XML docs + IntelliSense | ⭐⭐⭐⭐⭐ Auto-generated API docs |
| **Type Safety** | ⭐⭐⭐⭐⭐ Compile-time checking | ⭐⭐⭐⭐ Runtime with type hints |
| **Ecosystem** | ⭐⭐⭐⭐ .NET ecosystem | ⭐⭐⭐⭐⭐ Vast Python libraries |

## 🌟 Core Features (Both Implementations)

### 🤖 Telegram Bot Commands
- `/start` and `/help` - Interactive command guidance
- `/add` - Secure bank connection via SimpleFIN tokens
- `/accounts` and `/refresh` - Real-time account data with balance information
- `/remove` - Secure bank connection removal
- `/web` - Launch integrated WebApp interface

### 🌐 REST API Endpoints
- `GET /api/accounts?user_id={id}` - Retrieve user's bank connections
- **CORS enabled** for cross-origin requests
- **Error handling** with structured responses
- **Health checks** and monitoring endpoints

### 📱 Modern WebApp Interface
- **Telegram WebApp API** integration with native theming
- **Responsive design** for mobile and desktop
- **Real-time data** synchronization with bot and API
- **Enhanced UX** with loading states and error handling

### ⚙️ Advanced Configuration
- **Multi-environment** support (Development/Production)
- **Environment variables** for secure production deployment
- **Validation** with helpful error messages for developers
- **Flexible settings** for different deployment scenarios

## 🏗️ Project Structure

```
SimpleFinTelegramBot/
├── 📁 csharp/                    # C# (.NET 8) Implementation
│   ├── SimpleFinBot/             # Console Bot Application
│   ├── SimpleFinWebApi/          # ASP.NET Core API
│   ├── SimpleFinWebApp/          # Static WebApp
│   ├── .github/workflows/        # CI/CD Pipeline
│   └── README.md                 # C# Documentation
├── 📁 python/                    # Python Implementation
│   ├── SimpleFinBot/             # Async Python Bot
│   ├── SimpleFinWebApi/          # FastAPI Backend
│   ├── SimpleFinWebApp/          # Enhanced WebApp
│   └── README.md                 # Python Documentation
├── README.md                     # This file
├── DESCRIPTION.md                # Project overview
└── GITHUB_DESCRIPTION.md         # Repository metadata
```

## � Quick Start

### For C# (.NET 8):
```bash
cd csharp
dotnet restore
# Configure bot token in appsettings.json or environment variables
dotnet run --project SimpleFinWebApi  # Terminal 1
dotnet run --project SimpleFinBot     # Terminal 2
```

### For Python:
```bash
cd python/SimpleFinBot
pip install -r requirements.txt
# Configure bot token in config.json or environment variables
cd ../SimpleFinWebApi && pip install -r requirements.txt
python api.py          # Terminal 1
cd ../SimpleFinBot && python bot.py  # Terminal 2
```

## 🔒 Security & Best Practices

Both implementations include:
- ✅ **Secure token management** with environment variable support
- ✅ **Input validation** and sanitization
- ✅ **Parameterized database queries** preventing SQL injection
- ✅ **CORS configuration** for API security
- ✅ **Error handling** with user-friendly messages
- ✅ **Configuration validation** with startup checks

## 📚 Documentation

### Getting Started:
- 🔷 [C# Setup Guide](./csharp/README.md) - Complete .NET 8 setup instructions
- 🐍 [Python Setup Guide](./python/README.md) - Python installation and configuration
- ⚙️ [C# Configuration](./csharp/SimpleFinBot/BOT_CONFIGURATION.md) - Advanced C# configuration
- ⚙️ [Python Configuration](./python/PYTHON_CONFIGURATION.md) - Python configuration guide

### Technical Details:
- 📖 [Project Overview](./DESCRIPTION.md) - Architecture and design decisions
- 🏷️ [Repository Info](./GITHUB_DESCRIPTION.md) - GitHub metadata and tags

## 📋 Usage Workflow

1. **Setup**: Choose your preferred implementation (C# or Python)
2. **Configure**: Set up your Telegram bot token via @BotFather
3. **Deploy**: Run both the API server and bot application
4. **Connect**: Start a chat with your bot and use `/add` to connect banks
5. **Access**: Use bot commands or the WebApp interface to view account data

## 🧪 Development & Testing

### C# Development:
- **VS Code**: Complete development environment with tasks and debugging
- **GitHub Actions**: Automated CI/CD pipeline for testing and building
- **IntelliSense**: Full IDE support with compile-time error checking

### Python Development:
- **FastAPI Docs**: Automatic API documentation at `/docs`
- **Type Hints**: Full type safety with runtime validation
- **Hot Reload**: Development server with auto-restart on changes

## 🤝 Contributing

1. Choose your preferred implementation (C# or Python)
2. Fork the repository
3. Create a feature branch
4. Follow the coding standards for your chosen language
5. Submit a pull request with tests

## 📄 License

This project serves as a comprehensive template for SimpleFIN integration with Telegram bots in both C# and Python.

---

<div align="center">

**🔷 Choose C# for enterprise applications with high performance requirements**  
**🐍 Choose Python for rapid development and extensive ecosystem integration**

Both implementations provide identical functionality with language-specific optimizations!

</div>
