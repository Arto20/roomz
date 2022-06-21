from sqlalchemy import Column, Integer, String, Boolean

from app.core.db import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer)
    is_private = Column(Boolean)
