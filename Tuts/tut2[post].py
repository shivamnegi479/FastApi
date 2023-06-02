from fastapi import FastAPI
from fastapi.params import Body

import uvicorn
from pydantic import BaseModel
app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    rating:int

@app.post('/create')
def func(post:Post):
    print(post.dict())
    return {
        "data":post
    }


if __name__=="__main__":
    uvicorn.run(app=app,host="127.0.0.1",debug=True)