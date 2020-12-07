from common.keyboards import main_keyboard_markup
from common.states import NewMessageBotState, CommonBotState
from db.models import Room
from db.repositories import RoomRepository, UserRepository
from loader import bot
from ..utils.filters import check_state, apply_many, is_private_chat


@bot.message_handler(
    func=lambda m: apply_many(m, lambda mess: check_state(mess, NewMessageBotState.NEW_MESSAGE), is_private_chat))
def add_message(message):
    RoomRepository.add_message(message.db_user.target_room.id, message.text)