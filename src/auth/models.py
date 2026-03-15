from sqlmodel import Field, SQLModel,Column
import uuid
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import sqlalchemy as sa

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
            
        ))
        
    username:str
    email:str
    first_name  :str
    last_name:str
    is_active:bool = True 
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
        return f'<User {self.username}>'
    