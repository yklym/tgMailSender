from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from .types import CabinetKeyboardTypes as Keys
from .types import CommonKeyboardTypes

cabinet_keyboard_markup = ReplyKeyboardMarkup()

cabinet_keyboard_markup.row(KeyboardButton(Keys.CREAT_NEW_ROOM))
cabinet_keyboard_markup.row(KeyboardButton(CommonKeyboardTypes.RETURN_TO_MAIN_MENU))

__all__ = ['cabinet_keyboard_markup']
