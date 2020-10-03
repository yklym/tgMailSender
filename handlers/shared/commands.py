from common.text.default_commands import chat_info_text
from loader import bot


@bot.message_handler(commands=['chat_info'])
def chat_info(message):
    bot.reply_to(message, chat_info_text(message))


@bot.message_handler(commands=['rules'])
def show_rules(message):
    rules_message = bot.send_message(message.chat.id, "Init rules")
