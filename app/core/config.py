from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application Configuration
    app_name: str = "Falcon LLM API"
    version: str = "1.0.0"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    
    # Security Configuration
    secret_key: str  # Will read from lowercase environment variable
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Database Configuration
    database_url: str = "sqlite+aiosqlite:///./falcon.db"
    
    # CORS Configuration
    cors_origins: list = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False  # Allow any case for env variables

settings = Settings()