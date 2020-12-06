from ..models.room import Room
from ..models.types import ModelsTypes
from ..models.user import User

mock_user = User()
mock_user.id = 402359805
mock_user.name = 'Yaroslav'
mock_user.fullname = 'Yaroslav Klymenko'
mock_user.username = 'yKlymk'
mock_user.target_room = 'Test room'

mock_user_2 = User()
mock_user_2.id = 346192987
mock_user_2.name = 'Vlad'
mock_user_2.username = 'bot_chelovek_1234'
mock_user_2.target_room = 'Test room'

Storage = {
    ModelsTypes.USER: {
        mock_user.id: mock_user,
        mock_user_2.id: mock_user_2
    },
    ModelsTypes.ROOM: {
        'Test room': Room('Test room', mock_user.id, 'test room for tests')
    },
}
