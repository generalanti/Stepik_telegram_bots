# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types
import emoji

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def bot_start(message):
    start_kboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_catalog = types.KeyboardButton(text=emoji.emojize('Каталог :wrapped_gift:'))
    btn_profile = types.KeyboardButton(text=emoji.emojize('Мой профиль :bullseye:'))
    btn_faq = types.KeyboardButton(text=emoji.emojize('FAQ :candy:'))
    btn_bot_info = types.KeyboardButton(text=emoji.emojize('Информация о боте :information:'))
    btn_mailing = types.KeyboardButton(text=emoji.emojize('Сделать рассылку :megaphone:'))
    if message.chat.id == 5167752966:
         start_kboard.add(btn_catalog, btn_profile, btn_faq, btn_bot_info, btn_mailing)
    else:
        start_kboard.add(btn_catalog, btn_profile, btn_faq)

    bot.send_message(message.chat.id, 'Добро пожаловать в интернет-магазин', reply_markup=start_kboard)


bot.polling(none_stop=True)