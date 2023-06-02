from sqlalchemy import create_engine
DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fast1"
engine = create_engine(DATABASE_URL)
print(engine)
if engine:
    print("Connected")
else:
    print("Not connected")