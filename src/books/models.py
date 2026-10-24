from sqlmodel import SQLModel , Field , Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid 

class Book(SQLModel , table =True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        sa_column=Column(
        pg.UUID,
        nullable = False,
        primary_key=True,
        default= uuid.uuid4()
        )
    )
    title: str
    auther: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at : datetime
    update_at = datetime
        