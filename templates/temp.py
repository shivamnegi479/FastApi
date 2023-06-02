from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")
mypost=[
    {
    "title":"Post 1",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":1
    },
    {
    "title":"Post 2",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":2
    },
    {
    "title":"Post 3",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":3
    },
    {
    "title":"Post 4",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":4
    }
]


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    post=mypost
    return templates.TemplateResponse("item.html", {"request": request, "id": id,"post":post})

if __name__=="__main__":
    uvicorn.run(app="temp:app",host="localhost",reload=True)

