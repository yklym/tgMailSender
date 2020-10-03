from .base import BaseRepositoryClass
from ..models.types import ModelsTypes


class UserRepositoryClass(BaseRepositoryClass):
    _model = ModelsTypes.USER


UserRepository = UserRepositoryClass()

__all__ = ['UserRepository']
