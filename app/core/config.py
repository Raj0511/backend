from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Chatbot"
    API_V1_STR: str = "/api/v1"
    
    MONGO_URI: str
    DB_NAME: str = "chatbot_db"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


    GROQ_API_KEY: str

    class Config:
        env_file = "../.env"

settings = Settings()