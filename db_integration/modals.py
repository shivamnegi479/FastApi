from db import Base
from sqlalchemy import Column,String,Integer

class Employee(Base):
    __tablename__="Employee"
    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String,default=None)
    email=Column(String,default=None)
