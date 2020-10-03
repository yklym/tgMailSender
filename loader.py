import json

import telebot
from telebot.apihelper import _make_request as make_request

from common.bot_settings.commands_list import commands_list
from common.config import BOT_TOKEN

telebot.apihelper.ENABLE_MIDDLEWARE = True

# Set bot's commands
make_request(BOT_TOKEN, r'setMyCommands', params={'commands': json.dumps(commands_list)}, method='post')
bot = telebot.TeleBot(BOT_TOKEN)
