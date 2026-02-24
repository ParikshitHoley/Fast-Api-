
from sqlmodel import text,SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config

from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)



async def init_db():
    async with engine.begin() as conn:
        # Import models so metadata is registered
        from src.books.models import BookModel  

        # Create tables
        await conn.run_sync(SQLModel.metadata.create_all)