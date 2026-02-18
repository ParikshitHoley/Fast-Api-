from fastapi import FastAPI,status
from typing import List 
from pydantic import BaseModel  
from fastapi.exceptions import HTTPException
app = FastAPI()

books =[
  {
    "id": 1,
    "name": "Atomic Habits",
    "author": "James Clear",
    "genre": "Self-help",
    "publish_date": "2018-10-16",
    "price": 499
  },
  {
    "id": 2,
    "name": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Fiction",
    "publish_date": "1988-05-01",
    "price": 399
  },
  {
    "id": 3,
    "name": "Rich Dad Poor Dad",
    "author": "Robert T. Kiyosaki",
    "genre": "Finance",
    "publish_date": "1997-04-01",
    "price": 450
  },
  {
    "id": 4,
    "name": "Think and Grow Rich",
    "author": "Napoleon Hill",
    "genre": "Personal Development",
    "publish_date": "1937-01-01",
    "price": 350
  },
  {
    "id": 5,
    "name": "The Psychology of Money",
    "author": "Morgan Housel",
    "genre": "Finance",
    "publish_date": "2020-09-08",
    "price": 520
  }
]


class BookModel(BaseModel):
    id: int
    name: str
    author: str
    genre: str
    publish_date: str
    price: int
    
class BookModelUpdate(BaseModel):
    name: str
    author: str
    genre: str
   


@app.get("/books",response_model=List[BookModel],status_code=status.HTTP_200_OK )
async def get_books():
    return books

@app.get("/books/{book_id}",response_model=BookModel,status_code=status.HTTP_200_OK)
async def get_book(book_id: int ):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")  

@app.post("/books",response_model=BookModel,status_code=status.HTTP_201_CREATED)
async def add_book(book: BookModel): 
    new_book =  book.model_dump()
    books.append(new_book)
    return new_book

@app.patch("/books/{book_id}",response_model=BookModel,status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book_data: BookModelUpdate):
    
     for book in books:
        if book["id"] == book_id:
            book["name"] = book_data.name
            book["author"] = book_data.author
            book["genre"] = book_data.genre
            return book
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
 
@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
         