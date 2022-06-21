from fastapi import FastAPI

from app.api import rooms

app = FastAPI()


app.include_router(rooms.router)
