from .base import BaseRepository
from ..models.types import ModelsTypes


class UserRepository(BaseRepository):
    _model = ModelsTypes.USER
