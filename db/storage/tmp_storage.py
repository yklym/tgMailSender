from ..models.room import Room
from ..models.types import ModelsTypes
from ..models.user import User

mock_user = User()
mock_user.id = 402359805
mock_user.name = 'Yaroslav'
mock_user.fullname = 'Yaroslav Klymenko'
mock_user.username = 'yKlymk'

Storage = {
    ModelsTypes.USER: {
        mock_user.id: mock_user
    },
    ModelsTypes.ROOM: {
        'Test room': Room('Test room', mock_user.id, 'test room for tests')
    },
}
