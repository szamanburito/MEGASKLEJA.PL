import datetime as _dt
from pydantic import BaseModel

class _AdminBase(BaseModel):
    email: str
    username: str

class AdminCreate(_AdminBase):
    password: str
    login: str

class AdminResponse(_AdminBase):
    id: int
    class Config:
        orm_mode = True