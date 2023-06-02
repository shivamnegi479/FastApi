from sqlalchemy import  Column, ForeignKey, Integer, String,VARCHAR
from db import Base
class Blog(Base):
    __tablename__="blogs"
    id=Column(Integer,primary_key=True, index=True)
    title=Column(String)
    body=Column(String)

class user(Base):
    __tablename__="user"
    id=d=Column(Integer,primary_key=True, index=True)
    name=Column(String)
    email=Column(VARCHAR)
