from sys import prefix
from database import engine
import admins

from fastapi import FastAPI

app = FastAPI(
)

app.include_router(admins.router)

admins.models.Base.metadata.create_all(engine)

@app.get("/api")
async def get_home():
    return {"Hello": "World!"}