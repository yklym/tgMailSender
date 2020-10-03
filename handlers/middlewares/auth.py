from db.repositories import UserRepository
from loader import bot


@bot.middleware_handler(update_types=['message'])
def set_db_user(bot_instance, message):
    message.db_user = UserRepository.get_by_id(message.from_user.id)
