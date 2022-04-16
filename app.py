from fastapi import FastAPI
from routes.people import people

app = FastAPI(
    title="Sistema de Control de Acceso Vehicular"
)


app.include_router(people)
