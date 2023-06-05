from sqlalchemy import create_engine,String,Integer,Boolean,Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
pwd=quote_plus("26547234s@S")
SQLALCHEMY_DATABASE_URL = f"postgresql://shivam:{pwd}@localhost/fastpi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
