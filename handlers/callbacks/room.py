from common.keyboards import get_room_details_keyboard
from common.keyboards_inline.types import InlineKeyboardsType, CreatedRoomDetailsTypes
from db.repositories import RoomRepository, UserRepository
from handlers.utils.filters import check_callback
from loader import bot
from .utils import get_call_parameters


@bot.callback_query_handler(func=lambda call: check_callback(call.data, InlineKeyboardsType.ROOMS_DETAILS))
def rooms_details(call):
    room_id = get_call_parameters(call.data, InlineKeyboardsType.ROOMS_DETAILS)[0]
    room = RoomRepository.get_by_id(room_id)
    keyboard = get_room_details_keyboard(room.is_private)
    UserRepository.set_target_room(call.from_user.id, room_id)
    bot.send_message(call.message.chat.id, f'ROOM [{room.id}] details:',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: check_callback(call.data, CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS))
def created_rooms_details(call):
    room_id = get_call_parameters(call.data, CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS)[0]
    room = RoomRepository.get_by_id(room_id)
    keyboard = get_room_details_keyboard(room.is_private)
    UserRepository.set_target_room(call.from_user.id, room_id)
    bot.send_message(call.message.chat.id, f'Your room [{room.id}] details:',
                     reply_markup=keyboard)
