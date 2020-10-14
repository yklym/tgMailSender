from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from .types import CabinetKeyboardTypes as Keys

cabinet_keyboard_markup = ReplyKeyboardMarkup()

cabinet_keyboard_markup.row(KeyboardButton(Keys.CREAT_NEW_ROOM))

__all__ = ['cabinet_keyboard_markup']
