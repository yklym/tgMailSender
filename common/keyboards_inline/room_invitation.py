from .types import RoomInvitationInlineKeyboardType as Keys
from telebot import types


def room_invitation_inline_keyboard(room_id):
    room_details_kb = types.InlineKeyboardMarkup()
    details_button = types.InlineKeyboardButton('Join Room', callback_data=f'{Keys.ROOMS_INVITATION}_{room_id}')
    room_details_kb.add(details_button)

    return room_details_kb
