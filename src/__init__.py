from fastapi import FastAPI,status
from src.books.routes import books_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('server starting...')
    await init_db()
    yield
    print('server closing...')
    

version = "v1"  
app = FastAPI(
    title="Book Management API",
    description="A simple API for managing books",
    version=version,
    lifespan=lifespan
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["Books"] )