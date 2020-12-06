from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class UserRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.USER

    def set_state(self, id, state):
        self.storage[id].state = state

    def get_state(self, id):
        return self.storage[id].state

    def set_target_room(self, id, room_id):
        print(self.storage)
        print(self.storage[id])
        print(self.storage[id].target_room)
        print('----------------------------')
        self.storage[id].target_room = room_id
        return self.storage[id]


UserRepository = UserRepositoryClass()

__all__ = ['UserRepository']
