# Copilot Instructions

<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

## Project Overview
This is a SimpleFIN Telegram Bot solution that includes:
- **SimpleFinBot**: Console application for Telegram Bot integration
- **SimpleFinWebApi**: ASP.NET Core Web API backend for WebApp
- **SimpleFinWebApp**: Static HTML frontend for Telegram WebApp

## Architecture Guidelines
- Use SQLite database (`simplefin_multi_accounts.db`) for data persistence
- Both bot and API share the same database file
- Follow async/await patterns for all I/O operations
- Use proper error handling and logging
- Implement CORS for Web API to allow cross-origin requests

## Telegram Bot Features
- `/start` and `/help` commands for user guidance
- `/add` command to connect new banks via SimpleFIN tokens
- `/accounts` and `/refresh` commands to display account information
- `/remove` command to disconnect banks
- `/web` command to open the WebApp interface

## SimpleFIN Integration
- Handle base64-encoded setup tokens
- Make authenticated HTTP requests to SimpleFIN API
- Parse JSON responses for account data
- Store access URLs securely in database

## Database Schema
```sql
accounts (
    user_id INTEGER,
    access_url TEXT,
    bank_name TEXT,
    created_at TEXT,
    PRIMARY KEY (user_id, access_url)
)
```

## Security Considerations
- Store bot tokens in environment variables or secure configuration
- Use parameterized queries for database operations
- Validate all user inputs
- Handle SimpleFIN API credentials securely
