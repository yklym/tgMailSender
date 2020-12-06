from common.config import BOT_URL
from common.keyboards import remove_keyboard, cabinet_keyboard_markup, \
    main_keyboard_markup, return_to_main_menu_keyboard_markup
from common.keyboards.types import MainKeyboardTypes, CabinetKeyboardTypes, CommonKeyboardTypes, RoomDetailsTypes
from common.keyboards_inline import room_invitation_inline_keyboard, room_details_cb, created_room_details_cb
from common.states import CreateRoomBotState
from db.repositories import UserRepository, RoomRepository
from handlers.utils.filters import is_private_chat
from loader import bot


@bot.message_handler(func=is_private_chat, regexp=MainKeyboardTypes.CABINET)
def start(message):
    bot.send_message(message.chat.id, 'Your cabinet:', reply_markup=cabinet_keyboard_markup)


@bot.message_handler(func=is_private_chat, regexp=CabinetKeyboardTypes.CREAT_NEW_ROOM)
def create_new_room(message):
    UserRepository.set_state(message.db_user.id, CreateRoomBotState.GET_ROOM_NAME)
    bot.send_message(message.chat.id, 'New room:', reply_markup=remove_keyboard)


@bot.message_handler(func=is_private_chat, regexp=MainKeyboardTypes.MY_ROOMS)
def return_to_room(message):
    rooms_dict = RoomRepository.get_all_ids_by_user_id(message.db_user.id)
    bot.send_message(message.chat.id, 'Your Subscriptions:', reply_markup=return_to_main_menu_keyboard_markup)
    for room_name in rooms_dict:
        tmp_room = RoomRepository.get_by_id(room_name)
        bot.send_message(message.chat.id, f'Room:\nName: [{room_name}]\nDescription: [{tmp_room.description}]',
                         reply_markup=room_details_cb(room_name))


@bot.message_handler(func=is_private_chat, regexp=CommonKeyboardTypes.RETURN_TO_MAIN_MENU)
def return_to_main_menu(message):
    bot.send_message(message.chat.id, 'Main menu:', reply_markup=main_keyboard_markup)


@bot.message_handler(func=is_private_chat, regexp=RoomDetailsTypes.CREATE_INVITATION)
def get_room_invitation(message):
    response_text = f'{BOT_URL}?start={"_".join(message.db_user.target_room.split(" "))}'
    bot.send_message(message.chat.id, response_text)


@bot.message_handler(func=is_private_chat, regexp=CabinetKeyboardTypes.MY_ROOMS)
def send_created_rooms(message):
    rooms_dict = RoomRepository.get_all_ids_by_owner_id(message.db_user.id)
    bot.send_message(message.chat.id, 'Your Rooms:', reply_markup=return_to_main_menu_keyboard_markup)
    for room_name in rooms_dict:
        tmp_room = RoomRepository.get_by_id(room_name)
        bot.send_message(message.chat.id, f'Room:\nName: [{room_name}]\nDescription: [{tmp_room.description}]',
                         reply_markup=created_room_details_cb(room_name))
