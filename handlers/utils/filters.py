from common.types import ChatTypes


def is_private_chat(message):
    return message.chat.type == ChatTypes.PRIVATE


def is_group(message):
    return message.chat.type == ChatTypes.GROUP or message.chat == ChatTypes.SUPERGROUP


def is_authorized(message):
    return message.db_user


def apply_many(message, *filters):
    return all([filter_func(message) for filter_func in filters])
