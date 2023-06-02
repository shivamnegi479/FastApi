from fastapi import FastAPI
import uvicorn
app=FastAPI()

all_items=[
    {"name":"shivam"},
    {"name":"Atul"},
    {"name":"sanju"},
    {"name":"raj"},
    {"name":"bhau"},
    {"name":"mk"},
]

@app.get('/')
def read_item():
    return {
        "Message":"Welcome"
    }
@app.get('/item')
def read_item(skip:int =0, limit: int=10):
    return all_items[0:10]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.1.1", port=8000)