from common.states import CreateRoomBotState
from db.models import Room
from db.repositories import RoomRepository, UserRepository
from loader import bot
from ..utils.filters import check_state, apply_many, is_private_chat


@bot.message_handler(
    func=lambda m: apply_many(m, lambda mess: check_state(mess, CreateRoomBotState.GET_ROOM_NAME), is_private_chat))
def create_room(message):
    if RoomRepository.get_by_id(message.text):
        bot.reply_to(message, 'This name is already used')
    else:
        RoomRepository.insert(Room(message.text, message.chat.id))
        UserRepository.set_state(message.db_user.id, CreateRoomBotState.GET_ROOM_DESCRIPTION)
        bot.reply_to(message, 'Name saved, now add some description')
