from common.config import BOT_URL
from common.keyboards import remove_keyboard, cabinet_keyboard_markup, \
    main_keyboard_markup, return_to_main_menu_keyboard_markup
from common.keyboards.types import MainKeyboardTypes, CabinetKeyboardTypes, CommonKeyboardTypes, \
    CreatedRoomDetailsTypes, RoomDetailsTypes
from common.keyboards_inline import room_details_cb, created_room_details_cb, message_viewer_details_cb
from common.states import CreateRoomBotState, NewMessageBotState
from common.text import message_view_text
from db.repositories import UserRepository, RoomRepository
from handlers.utils.filters import is_private_chat
from loader import bot


@bot.message_handler(func=is_private_chat, regexp=MainKeyboardTypes.CABINET)
def start(message):
    bot.send_message(message.chat.id, 'Вітаємо у вашому кабінеті!:', reply_markup=cabinet_keyboard_markup)


@bot.message_handler(func=is_private_chat, regexp=CabinetKeyboardTypes.CREAT_NEW_ROOM)
def create_new_room(message):
    UserRepository.set_state(message.db_user.id, CreateRoomBotState.GET_ROOM_NAME)
    bot.send_message(message.chat.id, 'Почнемо створення кімнати з її назви:', reply_markup=remove_keyboard)


@bot.message_handler(func=is_private_chat, regexp=MainKeyboardTypes.MY_ROOMS)
def return_to_room(message):
    rooms_dict = RoomRepository.get_all_ids_by_user_id(message.db_user.id)
    bot.send_message(message.chat.id, '<b>Список підписок:</b>',
                     reply_markup=return_to_main_menu_keyboard_markup,
                     parse_mode='HTML')
    for room_name in rooms_dict:
        tmp_room = RoomRepository.get_by_id(room_name)
        user = UserRepository.get_by_id(message.db_user.id)
        is_muted = tmp_room.id in user.muted_list
        bot.send_message(message.chat.id, f'<b>Кімната</b>\n'
                                          f'<b>Назва:</b> {room_name}\n'
                                          f'<b>Опис:</b> {tmp_room.description}',
                         reply_markup=room_details_cb(room_name, is_muted),
                         parse_mode='HTML')


@bot.message_handler(func=is_private_chat, regexp=CommonKeyboardTypes.RETURN_TO_MAIN_MENU)
def return_to_main_menu(message):
    bot.send_message(message.chat.id, 'Вітаємо у головному меню:', reply_markup=main_keyboard_markup)


@bot.message_handler(func=is_private_chat, regexp=CreatedRoomDetailsTypes.CREATE_INVITATION)
def get_room_invitation(message):
    response_text = f'[Запрошення приєднатись до кімнати]({BOT_URL}?start={"_".join(message.db_user.target_room.split(" "))})'
    bot.send_message(message.chat.id, response_text, parse_mode='MarkdownV2')


@bot.message_handler(func=is_private_chat, regexp=CabinetKeyboardTypes.MY_ROOMS)
def send_created_rooms(message):
    rooms_dict = RoomRepository.get_all_ids_by_owner_id(message.db_user.id)
    bot.send_message(message.chat.id, '<b>Список створених кінмат:</b>:', reply_markup=return_to_main_menu_keyboard_markup)
    for room_name in rooms_dict:
        tmp_room = RoomRepository.get_by_id(room_name)
        bot.send_message(message.chat.id, f'<b>Кімната</b>\n'
                                          f'<b>Назва:</b> {room_name}\n'
                                          f'<b>Опис:</b> {tmp_room.description}'
                                          f'<b>Пароль:</b>:{tmp_room.password or "Не встановлено"}',
                         reply_markup=created_room_details_cb(room_name),
                         parse_mode='HTML')


@bot.message_handler(func=is_private_chat, regexp=CreatedRoomDetailsTypes.SEND_MESSAGE)
def send_message_to_room(message):
    UserRepository.set_state(message.db_user.id, NewMessageBotState.NEW_MESSAGE)
    bot.send_message(message.chat.id, 'Запишіть повідомлення:', reply_markup=remove_keyboard)


@bot.message_handler(func=is_private_chat, regexp=RoomDetailsTypes.GET_LAST_MESSAGES)
def send_message_to_room(message):
    target_room_id = message.db_user.target_room
    target_room = RoomRepository.get_by_id(target_room_id)
    pages_amount = len(target_room.messages)
    last_message = target_room.messages[pages_amount - 1]
    curr_page = pages_amount - 1
    bot.send_message(chat_id=message.chat.id,
                     text=message_view_text(curr_page, pages_amount, target_room_id, last_message),
                     reply_markup=message_viewer_details_cb(curr_page, pages_amount, target_room_id),
                     parse_mode="HTML")
