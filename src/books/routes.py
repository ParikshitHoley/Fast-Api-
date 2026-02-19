from src.books.book_data import books
from src.books.schemas import BookModel, BookModelUpdate
from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

books_router = APIRouter()


@books_router.get("/",response_model=List[BookModel],status_code=status.HTTP_200_OK )
async def get_books():
    return books

@books_router.get("/{book_id}",response_model=BookModel,status_code=status.HTTP_200_OK)
async def get_book(book_id: int ):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")  

@books_router.post("/",response_model=BookModel,status_code=status.HTTP_201_CREATED)
async def add_book(book: BookModel): 
    new_book =  book.model_dump()
    books.append(new_book)
    return new_book

@books_router.patch("/{book_id}",response_model=BookModel,status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book_data: BookModelUpdate):
    
     for book in books:
        if book["id"] == book_id:
            book["name"] = book_data.name
            book["author"] = book_data.author
            book["genre"] = book_data.genre
            return book
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
 
@books_router.delete("/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
         