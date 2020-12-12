from common.keyboards_inline import create_room_is_password_cb
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
        bot.reply_to(message, "Ім'я вже використано")
    else:
        message.db_user.tmp_room = Room(message.text, message.chat.id)
        UserRepository.set_state(message.db_user.id, CreateRoomBotState.GET_ROOM_DESCRIPTION)
        bot.reply_to(message, 'Назву збережено, тепер додайте опис кімнати')


@bot.message_handler(
    func=lambda m: apply_many(
        m,
        lambda mess: check_state(mess, CreateRoomBotState.GET_ROOM_DESCRIPTION),
        is_private_chat))
def create_description(message):
    message.db_user.tmp_room.description = message.text
    bot.send_message(
        message.chat.id,
        'Чи бажаєте обмежити доступ до кімнати з допомогою паролю?\n '
        'Це налаштування можна змінити пізніше',
        reply_markup=create_room_is_password_cb(message.db_user.id))

    RoomRepository.insert(message.db_user.tmp_room)


@bot.message_handler(
    func=lambda m: apply_many(
        m,
        lambda mess: check_state(mess, CreateRoomBotState.GET_ROOM_PASS),
        is_private_chat))
def save_pass(message):
    message.db_user.tmp_room.password = message.text
    UserRepository.set_state(message.db_user.id, CommonBotState.DEFAULT_STATE)
    RoomRepository.insert(message.db_user.tmp_room)
    bot.send_message(
        message.chat.id,
        'Створено кімнату: \n'
        f'Назва: {message.db_user.tmp_room.id}\n'
        f'Опис: {message.db_user.tmp_room.description}\n'
        f'Пароль: {message.db_user.tmp_room.password or "--"}\n',
        reply_markup=main_keyboard_markup)

    RoomRepository.insert(message.db_user.tmp_room)
