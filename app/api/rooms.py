from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.repository.rooms_repository import create_new_room, get_room_by_id, get_all_rooms, delete_room_by_id, \
    update_room_by_id
from app.schemas.room import Room, RoomUpdate, RoomCreate

router = APIRouter()


@router.get('/rooms', response_model=List[Room])
def get_rooms(db: Session = Depends(get_db)):
    return get_all_rooms(db)


@router.get('/rooms/{room_id}', response_model=Room)
def get_rooms(room_id, db: Session = Depends(get_db)):
    return get_room_by_id(db, room_id)


@router.post('/rooms', response_model=Room)
def create_room(input_data: RoomCreate, db: Session = Depends(get_db)):
    return create_new_room(db, input_data.name, input_data.owner_id, input_data.is_private)


@router.put('/rooms/{room_id}', response_model=Room)
def update_room(room_id: int, input_data: RoomUpdate, db: Session = Depends(get_db)):
    return update_room_by_id(
        room_id=room_id,
        name=input_data.name,
        owner_id=input_data.owner_id,
        is_private=input_data.is_private,
        db=db
    )


@router.delete('/rooms/{room_id}', response_model=Room)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = delete_room_by_id(room_id, db)
    if not room:
        raise HTTPException(status_code=404, detail='Item not found')
    return room
