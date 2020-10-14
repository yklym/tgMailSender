from handlers.utils.filters import is_private_chat
from loader import bot


@bot.message_handler(func=is_private_chat, commands=['start'])
def start(message):
    # if not message.db_user:
    #     UserRepository.insert(message.from_user)
    #     # notify_admin_chat(bot, f"User @{message.from_user.username} was added to the db")

    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}\n', reply_markup=main_keyboard_markup)
