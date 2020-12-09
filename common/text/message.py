def message_view_text(curr_page, page_amount, room_name, text):
    br_line = '\n'
    return (f'<b>          {room_name}          </b>' +
            br_line +
            f'============[{curr_page + 1} / {page_amount}]============' +
            br_line +
            br_line +
            text)
