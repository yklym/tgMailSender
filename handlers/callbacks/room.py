from common.keyboards import get_room_details_keyboard, created_room_keyboard_markup, main_keyboard_markup
from common.keyboards_inline import message_viewer_details_cb, room_details_cb
from common.keyboards_inline.types import InlineKeyboardsType, CreatedRoomDetailsTypes, MessageViewerKeyboardsType, \
    CreateRoomIsUsePasswordTypes
from common.states import CreateRoomBotState, CommonBotState
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
    bot.send_message(call.message.chat.id, f'Деталі кімнати [{room.id}]:',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: check_callback(call.data, CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS))
def created_rooms_details(call):
    room_id = get_call_parameters(call.data, CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS)[0]
    room = RoomRepository.get_by_id(room_id)
    UserRepository.set_target_room(call.from_user.id, room_id)
    bot.send_message(call.message.chat.id, f'Деталі кімнати [{room.id}](адмін):',
                     reply_markup=created_room_keyboard_markup)


@bot.callback_query_handler(func=lambda call: check_callback(call.data, MessageViewerKeyboardsType.SET_PAGE))
def send_message_to_room(call):
    params_list = get_call_parameters(call.data, CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS)
    curr_page, room_id = int(params_list[1]), params_list[2]
    target_room = RoomRepository.get_by_id(room_id)
    pages_amount = len(target_room.messages)
    room_message = target_room.messages[curr_page]

    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=message_view_text(curr_page, pages_amount, room_id, room_message),
                          reply_markup=message_viewer_details_cb(curr_page, pages_amount, room_id),
                          parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: check_callback(call.data, InlineKeyboardsType.TURN_NOTIFICATIONS_ON))
def set_notifications_on(call):
    room_id = get_call_parameters(call.data, InlineKeyboardsType.TURN_NOTIFICATIONS_ON)[0]
    room = RoomRepository.get_by_id(room_id)
    user_id = call.from_user.id
    UserRepository.set_room_notification(user_id, room_id, False)

    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f'<b>Кімната</b>\n'
                               f'<b>Назва:</b> {room_id}\n'
                               f'<b>Опис:</b> {room.description}',
                          reply_markup=room_details_cb(room_id, False),
                          parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: check_callback(call.data, InlineKeyboardsType.TURN_NOTIFICATIONS_OFF))
def set_notifications_off(call):
    room_id = get_call_parameters(call.data, InlineKeyboardsType.TURN_NOTIFICATIONS_OFF)[0]
    user_id = call.from_user.id
    room = RoomRepository.get_by_id(room_id)
    UserRepository.set_room_notification(user_id, room_id, True)

    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f'<b>Кімната</b>\n'
                               f'<b>Назва:</b> {room_id}\n'
                               f'<b>Опис:</b> {room.description}',
                          reply_markup=room_details_cb(room_id, True),
                          parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: check_callback(call.data, CreateRoomIsUsePasswordTypes.YES))
def set_rooom_pass_state(call):
    user_id = get_call_parameters(call.data, CreateRoomIsUsePasswordTypes.YES)[0]
    UserRepository.set_state(user_id, CreateRoomBotState.GET_ROOM_PASS)

    try:
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    except:
        pass
    finally:
        bot.send_message(chat_id=call.message.chat.id, text='Уведіть пароль:')


@bot.callback_query_handler(func=lambda call: check_callback(call.data, CreateRoomIsUsePasswordTypes.NO))
def skip_use_pass(call):
    user_id = get_call_parameters(call.data, CreateRoomIsUsePasswordTypes.NO)[0]
    user = UserRepository.get_by_id(user_id)
    UserRepository.set_state(user_id, CommonBotState.DEFAULT_STATE)
    RoomRepository.insert(user.tmp_room)

    try:
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    except:
        pass
    finally:
        bot.send_message(chat_id=call.message.chat.id,
                         text='Створено кімнату: \n'
                              f'Назва: {user.tmp_room.id}\n'
                              f'Опис: {user.tmp_room.description}\n'
                              f'Пароль: {user.tmp_room.password or "--"}\n',
                         reply_markup=main_keyboard_markup)
