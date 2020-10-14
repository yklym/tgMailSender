from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class RoomRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.ROOM


RoomRepository = RoomRepositoryClass()

__all__ = ['RoomRepository']
