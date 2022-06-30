from pydantic import BaseModel


class RoomBase(BaseModel):
    name: str
    owner_id: int
    is_private: bool


class RoomDB(RoomBase):
    id: int

    class Config:
        orm_mode = True


class Room(RoomDB):
    ...


class RoomDelete(BaseModel):
    ...


class RoomCreate(RoomBase):
    ...


class RoomUpdate(RoomBase):
    ...
