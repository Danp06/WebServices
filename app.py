from fastapi import FastAPI
from routes.people import people
from routes.Vehicles import vehicles

app = FastAPI(
    title="Sistema de Control de Acceso Vehicular"
)


app.include_router(people)
app.include_router(vehicles)