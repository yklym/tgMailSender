from common.types import ChatTypes
from db.repositories import UserRepository


def is_private_chat(message):
    return message.chat.type == ChatTypes.PRIVATE


def is_group(message):
    return message.chat.type == ChatTypes.GROUP or message.chat == ChatTypes.SUPERGROUP


def is_authorized(message):
    return message.db_user


def apply_many(message, *filters):
    return all([filter_func(message) for filter_func in filters])


def check_callback(data, target):
    return target in data


def has_subcommand(message, subcommand):
    return subcommand in message.text


def check_state(message, state):
    db_user = message.db_user
    if db_user:
        curr_state = UserRepository.get_state(db_user.id)
        return curr_state == state
    return false
