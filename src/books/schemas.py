
from pydantic import BaseModel

import uuid
from datetime import date, datetime

class BookSchema(BaseModel):
    
    id:uuid.UUID
    name: str
    author: str
    genre: str
    publish_date: date
    price: int
    created_at: datetime
    updated_at: datetime
    
    
class BookModelCreate(BaseModel):
    name: str
    author: str
    genre: str
    publish_date: date
    price: int
    
class BookModelUpdate(BaseModel):
    name: str
    author: str
    genre: str