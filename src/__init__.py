from fastapi import FastAPI,status
from src.books.routes import books_router

version = "v1"  
app = FastAPI(
    title="Book Management API",
    description="A simple API for managing books",
    version=version
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["Books"] )