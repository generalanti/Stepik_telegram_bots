# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(regexp=r'\d{11}')
def start(message):
    bot.send_message(message.chat.id, 'Это номер телефона')

@bot.message_handler(func=lambda message: True)
def start(message):
    bot.send_message(message.chat.id, 'Отправьте номер телефона')

bot.polling(none_stop=True)
