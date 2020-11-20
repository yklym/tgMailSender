from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from .types import MainKeyboardTypes as Keys

return_to_cabinet_keyboard_markup = ReplyKeyboardMarkup()

return_to_cabinet_keyboard_markup.row(KeyboardButton(Keys.CABINET))

__all__ = ['return_to_cabinet_keyboard_markup']
