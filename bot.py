# --*-- encoding: utf-8 --*--

import config
import telebot

bot = telebot.TeleBot(config.TOKEN)


def secret_word(message):
    return message.text == 'secret'


@bot.message_handler(func=secret_word)
def echo_all(message):
    bot.send_message(config.p_chat_id, 'введено секретное слово!')


bot.polling(none_stop=True)
