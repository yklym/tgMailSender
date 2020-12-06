from .types import RoomDetailsTypes as Keys
from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def get_room_details_keyboard(is_private=False):
    room_keyboard_markup = ReplyKeyboardMarkup()

    if not is_private:
        room_keyboard_markup.row(KeyboardButton(Keys.CREATE_INVITATION))

    room_keyboard_markup.row(KeyboardButton(Keys.DETAILS))
    room_keyboard_markup.row(KeyboardButton(Keys.GET_LAST_MESSAGES))
    room_keyboard_markup.row(KeyboardButton(Keys.SETTINGS))

    return room_keyboard_markup
