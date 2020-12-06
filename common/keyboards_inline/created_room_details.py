from telebot import types

from .types import CreatedRoomDetailsTypes


def created_room_details_cb(room_id):
    created_room_details_kb = types.InlineKeyboardMarkup()
    details_button = types.InlineKeyboardButton('Details',
                                                callback_data=f'{CreatedRoomDetailsTypes.CREATED_ROOMS_DETAILS}_{room_id}')
    created_room_details_kb.add(details_button)

    return created_room_details_kb
