from sqlalchemy import Column, Integer, String, Boolean

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    salt = Column(String)
    password_hash = Column(String)
