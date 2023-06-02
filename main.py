from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"data":{"hello": "word"}}




@app.get('/blog/{id}')

def show(id:int):

        
    return {"data":"row"}