from telebot import types

from .types import MessageViewerKeyboardsType as Types


def message_viewer_details_cb(curr_page, max_page, room_id):
    created_room_details_kb = types.InlineKeyboardMarkup()

    prev_many_btn = types.InlineKeyboardButton(
        '<<', callback_data=f'{Types.SET_PAGE}_{max(curr_page - 10, 0)}_{room_id}')
    prev_btn = types.InlineKeyboardButton(
        '<', callback_data=f'{Types.SET_PAGE}_{max(curr_page - 1, 0)}_{room_id}')
    next_btn = types.InlineKeyboardButton(
        '>', callback_data=f'{Types.SET_PAGE}_{min(curr_page + 1, max_page-1)}_{room_id}')
    next_many_btn = types.InlineKeyboardButton(
        '>>', callback_data=f'{Types.SET_PAGE}_{min(curr_page + 10, max_page-1)}_{room_id}')
    if max_page == 1:
        pass
    elif curr_page == 0:
        created_room_details_kb.row(next_btn, next_many_btn)
    elif curr_page + 1 == max_page:
        created_room_details_kb.row(prev_many_btn, prev_btn)
    else:
        created_room_details_kb.row(prev_many_btn, prev_btn, next_btn, next_many_btn)

    close_btn = types.InlineKeyboardButton('Закрити', callback_data=f'{Types.CLOSE_VIEWER}_{room_id}')
    created_room_details_kb.row(close_btn)

    return created_room_details_kb
