from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from .types import MainKeyboardTypes as Keys

main_keyboard_markup = ReplyKeyboardMarkup()

main_keyboard_markup.row(KeyboardButton(Keys.CABINET))
main_keyboard_markup.row(KeyboardButton(Keys.MY_ROOMS))
main_keyboard_markup.row(KeyboardButton(Keys.PAYMENTS), KeyboardButton(Keys.SETTINGS))
main_keyboard_markup.row(KeyboardButton(Keys.CONTACT), KeyboardButton(Keys.HELP))

__all__ = ['main_keyboard_markup']
