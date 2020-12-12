from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class UserRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.USER

    def set_state(self, id, state):
        id = int(id)
        self.storage[id].state = state

    def get_state(self, id):
        id = int(id)
        return self.storage[id].state

    def set_target_room(self, id, room_id):
        id = int(id)
        self.storage[id].target_room = room_id
        return self.storage[id]

    def set_room_notification(self, user_id, room_id, is_muted):
        user_id = int(user_id)
        if is_muted:
            if room_id not in self.storage[user_id].muted_list:
                self.storage[user_id].muted_list.append(room_id)
        else:
            self.storage[user_id].muted_list = list(
                filter(lambda muted_id: not muted_id == room_id, self.storage[user_id].muted_list))


UserRepository = UserRepositoryClass()

__all__ = ['UserRepository']
