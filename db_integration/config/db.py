from sqlalchemy import create_engine,MetaData
engine=create_engine("mysql+pymql://root@localhost:3306/test2")
conn=engine.connect()
meta=MetaData()

