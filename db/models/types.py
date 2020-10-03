from enum import Enum

from .base import Base
from .user import User


class ModelsTypes(Enum):
    BASE = 'base'
    USER = 'user'


models_list = {
    ModelsTypes.BASE: Base,
    ModelsTypes.USER: User,
}
