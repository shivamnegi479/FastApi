from fastapi import FastAPI,HTTPException,status,Response
from pydantic import BaseModel 
import uvicorn
app=FastAPI()
import psycopg2
from psycopg2.extras import RealDictCursor

class Post(BaseModel):
        title:str
        content:str
        published:bool
try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='26547234s@S',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("databse connection created successfully")
except:
    print("Not Connected")


@app.get('/')
def index():
    return {
        "Message":"Hello Welcome To Fastapi"
    }


@app.get('/post')
def get_post():
    cursor.execute("SELECT * from post")
    post=cursor.fetchall()
    return{
        "post":post
    }

@app.get('/post/{id}')
def fetchpost(id:int):
    cursor.execute("select * from post where id=(%s)"%(id))
    # print(post)
    post=cursor.fetchone()
    if post==None:
        return{
            "message":f"post with {id} is not exist "
        }
    return{
        "post":post
    }

@app.post('/create')
def create_post(post:Post = None):
    try:
        if post is None or not post.title or not post.content:
            raise HTTPException(status_code=200, detail="Missing required field: title or content")
        cursor.execute("INSERT INTO post(title,content,published) values(%s,%s,%s) RETURNING *" ,(post.title,post.content,post.published))
        conn.commit()
        return {"message": "Post created successfully!"}
    except HTTPException as he:
        # logging.error(f"Client error creating post: {he}")
        raise
    except Exception as e:
        # logging.error(f"Server error creating post: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# delete post 
@app.delete('/delete/{id}')
def delete(id:int):
    cursor.execute("DELETE from post where id= %s returning *"%id)
    delete_post=cursor.fetchone()
    print(delete_post)
    conn.commit()
    if delete_post==None:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail={"message":f"post with {id} does not exist"})
    return {
        "message":f"Post with {id} deleted successfully"
    }

# update post 

@app.put('/update/{id}')
def update(id:int,post:Post):
    cursor.execute("""update post set title=%s, content=%s, published=%s where id=%s returning *""",(post.title,post.content,post.published,id))
    data=cursor.fetchone()
    if data==None:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail={"message":f"post with {id} does not exist"})
    conn.commit()
    return{
        "data":data
    }


if __name__=="__main__":
    uvicorn.run(app=app,host='127.0.0.1',debug=True)