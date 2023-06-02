from  tut1 import base
from sqlalchemy import Column,Integer,String,Boolean

class Post(base):
    __tablename__="posts1"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,default=True)
    test=Column(String,nullable=True)


