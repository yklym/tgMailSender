from common.keyboards import main_keyboard_markup
from handlers.utils.filters import is_private_chat
from loader import bot


@bot.message_handler(func=is_private_chat, commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}\n', reply_markup=main_keyboard_markup)
