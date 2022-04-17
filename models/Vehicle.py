from msilib import datasizemask
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
class Vehicle(BaseModel):
	id: Optional[str]
	person:str
	status:bool
	placa:str
	fecha_ingreso: datetime = datetime.now() 
	anotaciones:Optional[str]