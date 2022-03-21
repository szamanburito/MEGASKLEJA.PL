from src.database import engine
import src.admins as admins

from fastapi import FastAPI

app = FastAPI(
)

app.include_router(admins.router)

admins.models.Base.metadata.create_all(engine)

@app.get("/api")
async def get_home():
    return {"Hello": "World!"}