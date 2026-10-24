from pydantic import BaseModel

class Book(BaseModel):
        id: int
        title: str
        auther: str
        publisher: str
        published_date: str
        page_count: int
        language: str
    
    
class BookUpdateModel(BaseModel):
    id: int
    title: str
    auther: str
    publisher: str
    published_date: str
    page_count: int
    language: str