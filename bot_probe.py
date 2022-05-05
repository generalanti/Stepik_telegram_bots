# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    start_kboard = types.InlineKeyboardMarkup(row_width=2)
    btn_menu = types.InlineKeyboardButton(text='Меню', callback_data='menu')
    start_kboard.add(btn_menu)
    bot.send_message(message.chat.id, 'Добро пожаловать в ресторан Chum Bucket', reply_markup=start_kboard)

@bot.callback_query_handler(func=lambda c:c.data)
def check_callback(callback):
    options_kboard = types.InlineKeyboardMarkup(row_width=2)
    btn_water = types.InlineKeyboardButton(text='Вода', callback_data='water')
    btn_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    btn_back_to_menu = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')

    if callback.data == 'menu':
        options_kboard.add(btn_water, btn_back)
        reply_msg = 'Вот наше меню:'
    elif callback.data == 'water':
        options_kboard.add(btn_back_to_menu)
        reply_msg = 'Воды нет, мы банкроты Т_Т'
    elif callback.data == 'back' or 'back_to_menu':
        start(callback.message)
        return
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=reply_msg,
                          reply_markup=options_kboard)

bot.polling(none_stop=True)