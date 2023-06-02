from fastapi import FastAPI,Response,status,HTTPException
import uvicorn
from pydantic import BaseModel

app=FastAPI()
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

def find_post(id):
    for i in mypost:
        if i['id']==id:
            return i

@app.get('/post/latest')
def latest():
    post=mypost[len(mypost)-1]
    return {
        "data":post
    }

@app.get('/post/all')
def all():
    post=mypost
    return {
        "data":post
    }
@app.get('/post/{id}')
def fetch_post(id:int,respons:Response):

    print(id)
    post=find_post(int(id))
    if not post:
        # respons.status_code=status.HTTP_404_NOT_FOUND
        # return {
        #     "message":f" post with id {id} not found"
        # }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message":f"Post with if {id} not found"})
    # print(find_post(id))
    return {
        "post":post
    }


if __name__=="__main__":
    uvicorn.run(app=app,host='127.0.0.1',debug=True)