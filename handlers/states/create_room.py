from common.keyboards import main_keyboard_markup
from common.states import CreateRoomBotState, CommonBotState
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
        message.db_user.tmp_room = Room(message.text, message.chat.id)
        UserRepository.set_state(message.db_user.id, CreateRoomBotState.GET_ROOM_DESCRIPTION)
        bot.reply_to(message, 'Name saved, now add some description')


@bot.message_handler(
    func=lambda m: apply_many(
        m,
        lambda mess: check_state(mess, CreateRoomBotState.GET_ROOM_DESCRIPTION),
        is_private_chat))
def create_description(message):
    message.db_user.tmp_room.description = message.text
    print(message.db_user.tmp_room)
    RoomRepository.insert(message.db_user.tmp_room)
    UserRepository.set_state(message.db_user.id, CommonBotState.DEFAULT_STATE)

    bot.send_message(
        message.chat.id,
        f'Saved room:\n, {message.db_user.tmp_room.id}\n',
        reply_markup=main_keyboard_markup)
