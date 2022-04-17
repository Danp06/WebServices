from bson import ObjectId
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.Vehicle import Vehicle
from schemas.Vehicle import vehicles_Entity, vehicle_Entity

from fastapi import APIRouter

vehicles = APIRouter()

@vehicles.get("/vehicles", response_model=list[Vehicle], tags=['vechicles'])
def get_all_vehicles():
    return vehicles_Entity(conn.local.vehicle.find())

@vehicles.post("/vehicles", tags=['vechicles'])
def post_vehicle(vehicle: Vehicle):
    new_vehicle = dict(vehicle)
    del new_vehicle["id"]

    id = conn.local.people.insert_one(new_vehicle).inserted_id
    register = conn.local.people.find_one({"_id": id})
    print(register)
    return str(register)

@vehicles.get("/vehicles/{placa}",response_model=Vehicle, tags=['vechicles'])
def get_vehicles(placa:str):
    return "specific vehicle"

@vehicles.put("/vehicles/{placa}",response_model=Vehicle, tags=['vechicles'])
def update_vehicle(placa:str):
    return "update veh"

@vehicles.put("/vehicles/{placa}",response_model=Vehicle, tags=['vechicles'])
def create_anotation(placa:str):
    return 'anotation'

@vehicles.get("/vehicles/findbystatus", response_model=Vehicle, tags=['vechicles'])
def get_vehicle_status():
    return "status"

