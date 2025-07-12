"""
SimpleFIN Web API - Python Version

A FastAPI-based REST API for accessing SimpleFIN banking data.
Provides endpoints for the Telegram WebApp to retrieve user bank information.
"""

import sqlite3
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class BankInfo(BaseModel):
    """Bank information model."""
    bank_name: str
    access_url: str


class BanksResponse(BaseModel):
    """Response model for banks endpoint."""
    banks: List[BankInfo]


class SimpleFinAPI:
    """SimpleFIN API main class."""
    
    def __init__(self, db_path: str = "simplefin_multi_accounts.db"):
        """Initialize the API with database path."""
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self) -> None:
        """Initialize SQLite database with required tables."""
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
    
    def get_user_banks(self, user_id: int) -> List[BankInfo]:
        """Get all banks for a specific user."""
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid user_id")
        
        banks = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT access_url, bank_name FROM accounts WHERE user_id = ?",
                (user_id,)
            )
            
            for access_url, bank_name in cursor.fetchall():
                banks.append(BankInfo(
                    bank_name=bank_name,
                    access_url=access_url
                ))
        
        return banks


# Create FastAPI app
app = FastAPI(
    title="SimpleFIN Web API",
    description="REST API for SimpleFIN banking data access",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create API instance
api = SimpleFinAPI()


@app.get("/api/accounts", response_model=BanksResponse)
async def get_accounts(user_id: int = Query(..., description="Telegram user ID")):
    """Get all bank accounts for a user."""
    banks = api.get_user_banks(user_id)
    return BanksResponse(banks=banks)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "SimpleFIN API is running"}


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "SimpleFIN Web API",
        "version": "1.0.0",
        "endpoints": {
            "accounts": "/api/accounts?user_id=<user_id>",
            "health": "/health",
            "docs": "/docs"
        }
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
