from fastapi import FastAPI
from pydantic import BaseModel

class Package(BaseModel):
    mac_address:str
    user_id:str


class Blog(BaseModel):
    name:str
    age:int

app=FastAPI()
@app.get('/')
async def word():
    return {"hello":"word"}

@app.get('/about/{id}')
async def about(id:int):
    return {"page":id}

@app.post("/blogs/")
async def post(blog:Blog):
    return blog


