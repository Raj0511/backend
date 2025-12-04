from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.knowledge import DocumentItem, EmbeddingChunk
from app.models.user import User
from app.models.chat import Chat, Message


async def init_db():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    

    database = client[settings.DB_NAME]
    
    await init_beanie(
        database=database,
        document_models=[
            User,
            Chat,
            Message,
            DocumentItem,
            EmbeddingChunk
        ]
    )
    
    print(f"Connected to MongoDB: {settings.DB_NAME}")