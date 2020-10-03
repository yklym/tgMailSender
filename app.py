import logging
import os

import telebot
from flask import Flask, request

from common.config import BOT_TOKEN, WH_SERVER_URL, SERVER_PORT
from handlers import bot

if __name__ == "__main__":
    # Starting server for webhooks in case its on deploy
    if "HEROKU" in list(os.environ.keys()):
        logger = telebot.logger
        telebot.logger.setLevel(logging.INFO)

        server = Flask(__name__)


        @server.route('/' + BOT_TOKEN, methods=['POST'])
        def getMessage():
            bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
            return "!", 200


        @server.route("/")
        def webhook():
            bot.remove_webhook()
            bot.set_webhook(url=WH_SERVER_URL + BOT_TOKEN)
            return "?", 200


        server.run(host="0.0.0.0", port=SERVER_PORT)
    else:
        # if development start long poling
        print("Bot started")
        bot.remove_webhook()
        bot.polling(none_stop=True)
