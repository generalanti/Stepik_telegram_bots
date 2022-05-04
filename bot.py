# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    start_kboard = types.InlineKeyboardMarkup(row_width=2)
    btn_like = types.InlineKeyboardButton(text='Люблю это', callback_data='loved')
    btn_dislike = types.InlineKeyboardButton(text='Это не люблю', callback_data='disliked')
    start_kboard.add(btn_like, btn_dislike)
    bot.send_message(message.chat.id, 'Выбери, что тебе нужно:', reply_markup=start_kboard)

@bot.callback_query_handler(func=lambda c:c.data)
def check_callback(callback):
    options_kboard = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton(text='Бикоончик', url='https://www.youtube.com/watch?v=xQ1pbGZ4VhA')
    btn_2 = types.InlineKeyboardButton(text='Пастила', url='https://www.youtube.com/watch?v=XEugAnTyLM4')
    btn_3 = types.InlineKeyboardButton(text='Сардины', url='https://www.youtube.com/watch?v=_qkzNN5_uu8')

    if callback.data == 'loved':
        options_kboard.add(btn_1, btn_2)
        reply_msg = 'Вот это люблю: '
    elif callback.data == 'disliked':
        options_kboard.add(btn_3)
        reply_msg = 'Вот это не люблю: '
    bot.send_message(callback.message.chat.id, reply_msg, reply_markup=options_kboard)

bot.polling(none_stop=True)