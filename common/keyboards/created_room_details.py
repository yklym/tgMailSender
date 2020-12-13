from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from .types import CreatedRoomDetailsTypes as Keys, CommonKeyboardTypes

created_room_keyboard_markup = ReplyKeyboardMarkup()

created_room_keyboard_markup.row(KeyboardButton(Keys.SEND_MESSAGE))
created_room_keyboard_markup.row(KeyboardButton(Keys.CREATE_INVITATION))
created_room_keyboard_markup.row(KeyboardButton(Keys.GET_LAST_MESSAGES))
created_room_keyboard_markup.row(KeyboardButton(Keys.GET_USER_LIST))
created_room_keyboard_markup.row(KeyboardButton(CommonKeyboardTypes.RETURN_TO_MAIN_MENU))
