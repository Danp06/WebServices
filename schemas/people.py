def person_entity(item) -> dict:
    return{
        "id": item["id"],
        "nombre": item["Nombre"],
        "rol": item["Rol"]
    }


def people_entity(entity) -> list:
    [person_entity(item) for item in entity]
