from fastapi import APIRouter

router = APIRouter()


@router.get('/rooms')
def get_rooms():
    return 'get room'


@router.post('/rooms')
def create_room():
    return 'created room'


@router.delete('/rooms')
def delete_room():
    return 'deleted room'

