from common.keyboards import main_keyboard_markup
from db.repositories import RoomRepository
from handlers.utils.filters import apply_many, is_private_chat, has_subcommand
from loader import bot


@bot.message_handler(func=is_private_chat, commands=['start'])
def start(message):
    sub_commands = message.text.split(' ')
    if len(sub_commands) > 1:
        room_id = ' '.join(sub_commands[1].split('_'))
        RoomRepository.add_participant(room_id, message.db_user.id)
        bot.send_message(message.chat.id, f'Successfully added to the room!')
    else:
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}\n', reply_markup=main_keyboard_markup)

