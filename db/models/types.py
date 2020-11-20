from enum import Enum

from .base import Base
from .user import User
from .room import Room

class ModelsTypes(Enum):
    BASE = 'base'
    USER = 'user'
    ROOM = 'room'


models_list = {
    ModelsTypes.BASE: Base,
    ModelsTypes.USER: User,
    ModelsTypes.ROOM: Room,
}
