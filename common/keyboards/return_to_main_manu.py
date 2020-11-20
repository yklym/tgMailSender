from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from .types import CommonKeyboardTypes as Keys

return_to_main_menu_keyboard_markup = ReplyKeyboardMarkup()

return_to_main_menu_keyboard_markup.row(KeyboardButton(Keys.RETURN_TO_MAIN_MENU))

__all__ = ['return_to_main_menu_keyboard_markup']
