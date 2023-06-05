from fastapi import FastAPI
import db
from db import engine
import modals
modals.Base.metadata.create_all(bind=engine)

app = FastAPI()


# # Dependency
# def get_db():
#     # db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()