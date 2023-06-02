from fastapi import FastAPI,status,HTTPException,Response
from pydantic import BaseModel
import uvicorn

class Post(BaseModel):
    id:int
    title:str
    content:str

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
def find_index(id):
    for i,p  in enumerate(mypost):
        if p['id']==id:
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

# fetch method 
@app.get('/post/{id}')
def fetch_post(id:int):
    print(id)
    post=find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message":f"Post with if {id} not found"})
    return {
        "post":post
    }

# delet method 
@app.delete('/post/{id}')
def delete_post(id:int):
    index=find_index(int(id))
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message":f"Post with id {id} not found"})
    mypost.pop(index)
    return {
        "message":f'post with id {id} deleted successfully',
    }


# post method 
@app.post('/create/{id}')
def create_post(id:int,post:Post):
    post.id=id
    print(post)
    return{
        "data":post
    }

# update method 
@app.put('/update/{id}')
def update_post(id:int, post:Post):
    index=find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message":f"Post with id {id} not found"})
    post_dict=post.dict()
    post_dict['id']=id
    mypost[index]=post_dict
    return{
        "data":post_dict
    }


if __name__=="__main__":
    uvicorn.run(app=app,host='127.0.0.1',debug=True)