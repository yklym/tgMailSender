from telebot import types

from .types import InlineKeyboardsType


def room_details_cb(room_id, is_muted):
    room_details_kb = types.InlineKeyboardMarkup()
    details_button = types.InlineKeyboardButton('Деталі',
                                                callback_data=f'{InlineKeyboardsType.ROOMS_DETAILS}_{room_id}')

    const_notification_btn_type = InlineKeyboardsType.TURN_NOTIFICATIONS_ON if is_muted else InlineKeyboardsType.TURN_NOTIFICATIONS_OFF
    notification_button = types.InlineKeyboardButton(
        ('Увімкнути' if is_muted else 'Вимнкути') + ' сповіщення',
        callback_data=f'{const_notification_btn_type}_{room_id}')

    room_details_kb.add(details_button)
    room_details_kb.add(notification_button)

    return room_details_kb
