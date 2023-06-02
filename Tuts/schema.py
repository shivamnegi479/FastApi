from pydantic import BaseModel
import datetime
from typing import Optional

class myblog(BaseModel):
    # id:int
    title:str
    description:Optional[str]=None



