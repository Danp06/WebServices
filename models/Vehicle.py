from typing import Optional
from pydantic import BaseModel

class Vehicle(BaseModel):
	id: Optional[str]
	person:str
	status:str
	placa:str
	fecha_ingreso:str 
	anotaciones:Optional[str]