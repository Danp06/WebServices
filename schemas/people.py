def person_entity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "nombre": item["nombre"],
        "rol": item["rol"]
    }


def people_entity(entity) -> list:
    [person_entity(item) for item in entity]
