from pydantic import BaseModel

class People(BaseModel):
    id:str
    nombre:str
    rol:int