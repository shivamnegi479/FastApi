from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get('/')
def index():
    return {
        "message":"hello word"
    }

@app.get('/items/{i_id}')
def get_items(i_id: int):
    return {
        "item":f"item {i_id}" 
    }

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}