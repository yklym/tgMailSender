from telebot import types

from .types import CreateRoomIsUsePasswordTypes as Types


def create_room_is_password_cb(user_id):
    create_room_pass_kb = types.InlineKeyboardMarkup()

    create_room_pass_kb.row(
        types.InlineKeyboardButton('Так', callback_data=f'{Types.YES}_{user_id}'),
        types.InlineKeyboardButton('Hi', callback_data=f'{Types.NO}_{user_id}')
    )

    return create_room_pass_kb
