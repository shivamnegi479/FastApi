from sqlalchemy import Column, Integer, String,exists
from sqlalchemy import create_engine,String,Integer,Boolean,Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from urllib.parse import quote_plus
from pydantic import BaseModel
import uvicorn

from fastapi import FastAPI,HTTPException
app=FastAPI()



pwd=quote_plus("26547234s@S")

SQLALCHEMY_DATABASE_URL = f"postgresql://shivam:{pwd}@localhost/fastapi"

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    with engine.connect() as connection:
        pass
    print("Connection to the database established successfully!")
except OperationalError as e:
    print(f"Failed to establish a connection to the database. Error: {str(e)}")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Employee(Base):
    __tablename__ = "Employee"
    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String, unique=True, index=True)
    emp_email = Column(String, unique=True, index=True)
    emp_password = Column(String)




Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
class empreate(BaseModel):
    emp_name: str
    emp_email: str
    emp_password: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users/")
async def create_user(user: UserCreate):
    db = SessionLocal()
    email_exists = db.query(exists().where(User.email == user.email)).scalar()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already exists")
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/emp/")
async def create_emp(employee: empreate):
    db = SessionLocal()
    emp_email_exists = db.query(exists().where(Employee.emp_email == employee.emp_email)).scalar()
    if emp_email_exists:
        raise HTTPException(status_code=400, detail="Employee email already exists")
    emp_user = Employee(emp_name=employee.emp_name, emp_email=employee.emp_email, emp_password=employee.emp_password)
    db.add(emp_user)
    db.commit()
    db.refresh(emp_user)
    return emp_user

if __name__=="__main__":
    uvicorn.run(app="ceate_tabel:app",host="localhost",reload=True)