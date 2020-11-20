from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class UserRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.USER

    def set_state(self, id, state):
        self.storage[id].state = state

    def get_state(self, id):
        return self.storage[id].state


UserRepository = UserRepositoryClass()

__all__ = ['UserRepository']
