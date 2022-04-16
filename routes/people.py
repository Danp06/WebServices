from fastapi import APIRouter
from config.db import conn
from schemas.people import people_entity, person_entity
from models.people import People

people = APIRouter()


@people.get('/people')
def list_people():
    return people_entity(conn.local.people.find())


@people.post('/people')
def create_people(person: People):
    new_person = dict(person)
    id = conn.local.people.insert_one(new_person).inserted_id
    return str(id)


@people.get('/people/{id}')
def find_person():
    return "Tomando Datos"


@people.put('/people/{id}')
def update_person():
    return "Tomando Datos"


@people.delete('/people/{id}')
def delete_person():
    return "Tomando Datos"
