from db.storage import Storage
from ..models.types import ModelsTypes, models_list


class BaseRepositoryClass:
    _model: ModelsTypes = models_list[ModelsTypes.BASE]

    def get_by_id(self, id):
        if id in self.storage:
            return self.storage[id]

    def insert(self, entity) -> bool:
        if entity.id:
            self.storage[entity.id] = entity
            return True
        else:
            new_id = self.storage.keys()[-1].id + 1
            self.storage[new_id] = entity
            return True

    def delete_by_id(self, id) -> bool:
        try:
            del self.storage[id]
            return True
        except e:
            print(e)
            return False

    def update(self, id, entity):
        self.storage[id] = entity

    @property
    def storage(self) -> dict:
        return Storage[self._model]

    @property
    def model_type(self):
        return models_list[_model]


BaseRepository = BaseRepositoryClass()
