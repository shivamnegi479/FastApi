from fastapi import FastAPI,Depends
import uvicorn
import psycopg2
from sqlalchemy.orm import session
from psycopg2.extras import RealDictCursor
import modals
from tut1 import engine
from tut1 import sessionlocal
modals.base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/sqlalchamy')
def test_post(db:session=Depends(get_db)):
    return{
        "Status":"sucess"
    }
if __name__=="__main__":
    uvicorn.run('main:app',host='127.0.0.1',port=8080,reload=True)
