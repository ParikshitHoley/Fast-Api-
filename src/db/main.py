
from sqlmodel import text,SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

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
        
async def get_session()->AsyncSession:
    Session= sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    async with Session() as session:
        yield session
            