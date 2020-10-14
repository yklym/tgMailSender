from common.keyboards import cabinet_keyboard_markup, remove_keyboard
from common.keyboards.types import MainKeyboardTypes, CabinetKeyboardTypes
from handlers.utils.filters import is_private_chat
from loader import bot
from db.repositories import UserRepository
from common.states import CreateRoomBotState


@bot.message_handler(func=is_private_chat, regexp=MainKeyboardTypes.CABINET)
def start(message):
    bot.send_message(message.chat.id, 'Your cabinet:', reply_markup=cabinet_keyboard_markup)


@bot.message_handler(func=is_private_chat, regexp=CabinetKeyboardTypes.CREAT_NEW_ROOM)
def start(message):
    UserRepository.set_state(message.db_user.id, CreateRoomBotState.GET_ROOM_NAME)
    bot.send_message(message.chat.id, 'New room:', reply_markup=remove_keyboard)
