from src.books.book_data import books
from src.books.models import BookModel
from typing import List
from fastapi import APIRouter, status,Depends
from fastapi.exceptions import HTTPException
from src.db.main import get_session
from src.books.services import BookService
from sqlalchemy.ext.asyncio.session import AsyncSession
import uuid
from src.books.schemas import BookModelCreate, BookModelUpdate

books_router = APIRouter()
book_service = BookService()

# get all books
@books_router.get("/",response_model=List[BookModel],status_code=status.HTTP_200_OK )
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

# get book by id
@books_router.get("/{book_id}",response_model=BookModel,status_code=status.HTTP_200_OK)
async def get_book(book_id:uuid.UUID,session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book_by_id(book_id,session)       
    if book: 
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")  

     

# create new book
@books_router.post("/",response_model=BookModel,status_code=status.HTTP_201_CREATED)
async def add_book(book: BookModelCreate,session: AsyncSession = Depends(get_session)): 
    new_book = await book_service.add_book(book,session)
    return new_book


# update book
@books_router.patch("/{book_id}",response_model=BookModel,status_code=status.HTTP_200_OK)
async def update_book(book_id: uuid.UUID, book_data: BookModelUpdate,session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(book_id,book_data,session)
    if updated_book:
        return updated_book
    else:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
 
 # delete book
@books_router.delete("/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: uuid.UUID,session: AsyncSession = Depends(get_session)):
    deleted = await book_service.delete_book(book_id,session)
    if deleted:
        return
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 
         