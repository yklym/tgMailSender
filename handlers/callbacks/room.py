from common.keyboards_inline.types import InlineKeyboardsType
from db.repositories import RoomRepository
from handlers.utils.filters import check_callback
from loader import bot
from .utils import get_call_parameters


@bot.callback_query_handler(func=lambda call: check_callback(call.data, InlineKeyboardsType.ROOMS_DETAILS))
def rooms_details(call):
    room_id = get_call_parameters(call.data, InlineKeyboardsType.ROOMS_DETAILS)[0]
    room = RoomRepository.get_by_id(room_id)
    bot.send_message(call.message.chat.id, 'ROOM INFO HERE :)')