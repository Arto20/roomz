from sqlalchemy.orm import Session

from app.models.room import Room


def create_new_room(db: Session, name: str, owner_id: int, is_private: bool):
    new_room = Room(
        name=name,
        owner_id=owner_id,
        is_private=is_private
    )

    db.add(new_room)
    db.commit()

    return new_room


def get_room_by_id(db: Session, room_id: int):
    return db.query(Room).filter(Room.id == room_id).first()


def get_all_rooms(db: Session):
    return db.query(Room).all()


def update_room_by_id(room_id: int, name: str, owner_id: int, is_private: bool, db: Session):
    room = db.query(Room).filter(Room.id == room_id).first()
    room.name = name
    room.owner_id = owner_id
    room.is_private = is_private

    db.add(room)
    db.commit()

    return room


def delete_room_by_id(room_id: int, db: Session):
    room = db.query(Room).filter(Room.id == room_id).first()
    db.query(Room).filter(Room.id == room_id).delete()
    db.commit()
    return room
