from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,String,Integer,Float
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_WARN_20=1
SQLALCHEMY_SILENCE_UBER_WARNING=1
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/fast1"
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    print("Database connection successful")
    connection.close()
except OperationalError as e:
    print(f"Error connecting to the database: {e}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)
    salary = Column(Float)
Base.metadata.create_all(bind=engine)