from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class RoomRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.ROOM

    def get_all_ids_by_user_id(self, user_id):
        return {key: value for (key, value) in self.storage.items() if value.owner_id == user_id}


RoomRepository = RoomRepositoryClass()

__all__ = ['RoomRepository']
