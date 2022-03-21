import datetime as _dt
import sqlalchemy as _sql

import gallery.database as _db

class Gallery(_db.Base):
    __tablename__ = "gallery"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    desctiption = _sql.Column(_sql.String, index=True)
    image = _sql.Column(_sql.LargeBinary, default=bytearray())
    original_image = _sql.Column(_sql.LargeBinary, default=bytearray())
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

class Messages(_db.Base):
    __tablename__ = "messages"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, index=True)
    title = _sql.Column(_sql.String, index=True)
    desctiption = _sql.Column(_sql.String, index=True)
    image = _sql.Column(_sql.LargeBinary, default=bytearray())
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)