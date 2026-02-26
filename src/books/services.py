from src.books.models import BookModel
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select ,desc
from src.books.schemas import BookModelCreate, BookModelUpdate

class BookService:
    async def get_all_books(self,session:AsyncSession):
        statement = select(BookModel).order_by(desc(BookModel.created_at))
        result = await session.execute(statement)
        books = result.all()
        return [book[0].model_dump() for book in books]
     
    async def get_book_by_id(self,book_id,session:AsyncSession):    
        statement = select(BookModel).where(BookModel.id == book_id)
        result = await session.execute(statement)
        book = result.first()
        return book[0] if book else None
    
    async def add_book(self,book:BookModelCreate,session:AsyncSession):
        book_to_create = book.model_dump()
        new_book = BookModel(**book_to_create)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book.model_dump()
    
    async def update_book(self,book_id,book_data:BookModelUpdate,session:AsyncSession):
        book_to_update = await self.get_book_by_id(book_id,session)
        if book_to_update:
            update_book_dict = book_data.model_dump(exclude_unset=True)
            for key, value in update_book_dict.items():
                setattr(book_to_update, key, value)
            session.add(book_to_update)
            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update.model_dump()
        else:
            return None
    
    async def delete_book(self,book_id,session:AsyncSession):
        book_to_delete = await self.get_book_by_id(book_id,session)
        if book_to_delete:
            await session.delete(book_to_delete)
            await session.commit()
            return True
        else:
            return None