from fastapi import FastAPI
from routes.people import people

app = FastAPI()


app.include_router(people)
