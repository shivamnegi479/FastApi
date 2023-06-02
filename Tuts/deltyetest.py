from fastapi import FastAPI,HTTPException,status,Response
from pydantic import BaseModel 
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='26547234s@S',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("databse connection created successfully")
except:
    print("Not Connected")

query="SELECT * from post where id= (%s)"%17
post=cursor.execute(query)
a=cursor.fetchone()
print(a)