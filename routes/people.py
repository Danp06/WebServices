from bson import ObjectId
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.people import People
from schemas.people import people_entity, person_entity

people = APIRouter()


@people.get('/people', response_model=list[People], tags=["People"])
def list_people():
    return people_entity(conn.local.people.find())


@people.post('/people', response_model=People, tags=["People"])
def create_people(person: People):
    new_person = dict(person)
    del new_person["id"]

    id = conn.local.people.insert_one(new_person).inserted_id
    person = conn.local.people.find_one({"_id": id})
    return person_entity(person)


@people.get('/people/{id}', response_model=People, tags=["People"])
def find_person(id: str):
    return person_entity(conn.local.people.find_one({"_id": ObjectId(id)}))


@people.put('/people/{id}', response_model=People, tags=["People"])
def update_person(id: str, person: People):
    conn.local.people.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(person)})
    return person_entity(conn.local.people.find_one({"_id": ObjectId(id)}))


@people.delete('/people/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["People"])
def delete_person(id: str):
    person_entity(conn.local.people.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
