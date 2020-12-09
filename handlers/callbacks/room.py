from common.keyboards import get_room_details_keyboard, created_room_keyboard_markup
from common.keyboards_inline import message_viewer_details_cb
from common.keyboards_inline.types import InlineKeyboardsType, CreatedRoomDetailsTypes, MessageViewerKeyboardsType
from common.text import message_view_text
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
    UserRepository.set_target_room(call.from_user.id, room_id)
    bot.send_message(call.message.chat.id, f'Your room [{room.id}] details:',
                     reply_markup=created_room_keyboard_markup)


@bot.callback_query_handler(func=lambda call: check_callback(call.data, MessageViewerKeyboardsType.SET_PAGE))
def send_message_to_room(call):
    params_list = get_call_parameters(call.data, CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS)
    curr_page, room_id = int(params_list[1]), params_list[2]
    print('----------------')
    print(curr_page)
    target_room = RoomRepository.get_by_id(room_id)
    pages_amount = len(target_room.messages)
    room_message = target_room.messages[curr_page]


    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=message_view_text(curr_page, pages_amount, room_id, room_message),
                          reply_markup=message_viewer_details_cb(curr_page, pages_amount, room_id),
                          parse_mode="HTML")

