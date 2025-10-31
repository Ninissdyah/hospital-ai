from pydantic import BaseModel #set struktur json
from typing import List #definisikan list

class inputData(BaseModel):
    gender: str
    age: int
    symptoms: List[str]