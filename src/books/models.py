from sqlmodel import SQLModel, Field, Column
import uuid
from datetime import date, datetime
import sqlalchemy.dialects.postgresql as pg
import sqlalchemy as sa
from pydantic import ConfigDict


class BookModel(SQLModel, table=True):
    
    __tablename__ = "books"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            nullable=False
        )
    )

    name: str
    author: str
    genre: str
    publish_date: date
    price: int

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now()
        )
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
            onupdate=sa.func.now()
        )
    )
    
    def __repr__(self):
        return f'<BookModel {self.name}>'