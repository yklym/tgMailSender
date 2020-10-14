from db.models import User
from db.repositories import UserRepository
from loader import bot


@bot.middleware_handler(update_types=['message'])
def set_db_user(bot_instance, message):
    db_user = UserRepository.get_by_id(message.from_user.id)
    if not db_user:
        UserRepository.insert(User(message.from_user))
        message.db_user = UserRepository.get_by_id(message.from_user.id)
    else:
        message.db_user = db_user
