
from pydantic import BaseModel  



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