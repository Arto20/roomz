from fastapi import FastAPI

from api import rooms

app = FastAPI()


app.include_router(rooms.router)