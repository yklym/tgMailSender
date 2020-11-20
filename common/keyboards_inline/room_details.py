from telebot import types

from .types import InlineKeyboardsType


def room_details_cb(room_id):
    room_details_kb = types.InlineKeyboardMarkup()
    details_button = types.InlineKeyboardButton('Details', callback_data=f'{InlineKeyboardsType.ROOMS_DETAILS}_{room_id}')
    room_details_kb.add(details_button)

    return room_details_kb
