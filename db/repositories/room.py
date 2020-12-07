from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class RoomRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.ROOM

    def get_all_ids_by_user_id(self, user_id):
        return {key: value for (key, value) in self.storage.items() if user_id in value.participants_ids }

    def get_all_ids_by_owner_id(self, owner_id):
        return {key: value for (key, value) in self.storage.items() if value.owner_id == owner_id}

    def add_participant(self, room_id, user_id):
        room = self.storage[room_id]
        if not user_id in room.participants_ids:
            room.participants_ids.append(user_id)

    def add_message(self, room_id, text):
        self.storage[room_id].messages.append(text)

RoomRepository = RoomRepositoryClass()

__all__ = ['RoomRepository']
