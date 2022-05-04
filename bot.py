# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Для того чтобы получить секретную информацию, отправь команду /getsecretinfo')

@bot.message_handler(commands=['getsecretinfo'])
def bot_start(message):
    inline_kboard = types.InlineKeyboardMarkup(row_width=1)
    btn_secret = types.InlineKeyboardButton(text='Секретная информация', url='https://www.youtube.com/watch?v=FuJM-90oMvo')
    inline_kboard.add(btn_secret)

    bot.send_message(message.chat.id, 'ХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА', reply_markup=inline_kboard)


bot.polling(none_stop=True)