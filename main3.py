from typing import Optional
from getmac import get_mac_address as gma
mac_add=gma()
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # mac_add:str=mac_add

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item