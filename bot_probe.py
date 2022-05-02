# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def bot_chat(message):
    start_kboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Catalog = types.KeyboardButton(text="Каталог")
    Info = types.KeyboardButton(text="Информация")
    start_kboard.add(Catalog, Info)
    bot.send_message(message.chat.id, "Добро пожаловать в магазин цифровых товаров", reply_markup=start_kboard)







bot.polling(none_stop=True)