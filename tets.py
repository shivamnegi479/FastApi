# from fastapi import FastAPI

# from typing import Optional

# app=FastAPI()

# @app.get('/')
# async def main():
#     return {
#         "name":"shivam"
#     }




import requests

re=requests.post("https://reqres.in/api/users?page=2")

print(re)
# data=re.json()
# result=data["data"]
# print(result)
# name=[]
# email=[]
# for i in result:
#     email.append(i["email"])
#     name.append(i["first_name"]+" "+i["last_name"])

# # for i,j in zip(name,email):
# #     print(f"{i} : {j}")


# import pandas as pd

# df=pd.DataFrame(columns=["Name","Email"])
# df["Name"]=pd.Series(name)
# df["Email"]=pd.Series(email)
# df.to_excel('Data.xlsx',index=None)


