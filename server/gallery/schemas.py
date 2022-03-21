import datetime as _dt
from msilib.schema import Binary
from pydantic import BaseModel


class _BaseImage(BaseModel):
    title: str
    description: str
    original_image: bytearray

class _BaseMessage(BaseModel):
    email: str
    title: str
    description: str
    image: bytearray

class CreateImage(_BaseImage):
    pass

class CreateMessafe(_BaseImage):
    pass