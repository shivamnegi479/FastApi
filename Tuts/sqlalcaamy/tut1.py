from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote


password = "26547234s@S"
encoded_password = quote(password, safe="")

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@host/database"
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{encoded_password}@localhost/fastapi"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal=sessionmaker(autocommit=False,bind=engine,autoflush=False)
base=declarative_base()
