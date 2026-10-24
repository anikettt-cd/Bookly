# webserver basics (path & query params , request body ,header)

from fastapi import FastAPI , Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message " : "hello world" }

@app.get('/greet')
async def greet_name(name : Optional[str] = "User" ,age:int = 0) -> dict:
    return {"message" : f"Hello {name}" , "age" : age}

@app.get('/verify')
async def verify_customer(Customer_ID:Optional[int] = "45") -> dict:
    return {"message" : f"{Customer_ID} is verified" }

class BookCreateModel(BaseModel):
    title : str
    author : str
    

@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {
        "title" : book_data.title ,
        "author" : book_data.title
    }
    
@app.get('/get_headers')
async  def get_header( 
    accept:str = Header(None) ,
    content_type : str = Header(None),
    user_agent: str = Header(None) , 
    host : str = Header(None)
):
    request_headers = {}
    request_headers["accept"] = accept
    request_headers["content-type"] = content_type
    request_headers["user-agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
    
