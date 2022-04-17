def vehicle_Entity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "person": str(item["person"]),
        "status": str(item["status"]),
        "placa": str(item["placa"]),
        "fecha_ingreso": str(item["fecha_ingreso"]),
        "anotaciones": str(item["anotaciones"])
    }

def vehicles_Entity(entity) -> list:
    return [vehicle_Entity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
