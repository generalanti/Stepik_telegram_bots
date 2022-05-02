# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types
import emoji

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def bot_start(message):
    start_kboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_buy = types.KeyboardButton(text=emoji.emojize('Купить :wrapped_gift:'))
    start_kboard.add(btn_buy)
    bot.send_message(message.chat.id, 'Добро пожаловать в интернет-магазин "Полезные товары"',\
                     reply_markup=start_kboard)


@bot.message_handler(regexp=r'Купить')
def select_buttons(message):
    pick_kboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_item1 = types.KeyboardButton(text='Камень с глазами')
    btn_back = types.KeyboardButton(text='Назад')
    pick_kboard.add(btn_item1, btn_back)
    bot.send_message(message.chat.id, 'Что хотите купить?', reply_markup=pick_kboard)


@bot.message_handler(regexp=r'Камень с глазами')
def show_item(message):
    item1_text = 'Товар: Камень с глазами\nЦена: 1000$\nВ наличии: 2'
    bot.send_photo(message.chat.id, r'https://ucarecdn.com/e3c749ec-5426-40f9-9060-20f7a236cb4b/',\
                   item1_text)

@bot.message_handler(regexp=r'Назад')
def navigate_back(message):
    bot_start(message)



bot.polling(none_stop=True)