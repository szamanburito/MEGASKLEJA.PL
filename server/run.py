from sys import prefix
from database import engine
import admins

from fastapi import FastAPI

app = FastAPI(
    prefix="/api"
)

app.include_router(admins.router)

admins.model.Base.metadata.create_all(engine)

@app.get("/")
async def get_home():
    return {"Hello": "World!"}