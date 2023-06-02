from fastapi import FastAPI
import uvicorn
# from pydantic import BaseModel
# from typing import Optional
# from uvicorn import
import schema
import model
from db import engine
app=FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return{
        "Message":"Hello Word"
    }


@app.post('/blog')
def create_blog(request:schema.myblog):
    return request


# class Item(BaseModel):
#     name:str
#     description:Optional[str]=None
#     age:Optional[int]=None
# @app.post("/items")
# def create_item(item:Item):
#     return f'item created successfully {item.name}'
if __name__=="__main__":
    uvicorn.run(app=app,host='127.0.0.1',port=8000, debug=True)