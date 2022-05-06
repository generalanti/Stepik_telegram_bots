# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types
import re

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    start_kboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_solve = types.KeyboardButton(text='Решить квадратное уравнение')
    start_kboard.add(btn_solve)
    bot.send_message(message.chat.id, 'Привет, что тебя интересует?', reply_markup=start_kboard)


@bot.message_handler(func=lambda message: message.text == 'Решить квадратное уравнение')
def register(message):
    sent = bot.reply_to(message, 'Введите коэффициенты ax^2 + bx + c в виде: a b c')
    bot.register_next_step_handler(sent, calc)




# TODO: проверить алгоритм решения уравнения
def calc(message):
    str1 = message.text
    result = re.search(r'-?\d+\s-?\d+\s-?\d+', str1)
    if result:
        bot.send_message(message.chat.id, 'Коэффициенты введены верно, начинаю решать уравнение')
        str1 = result.group(0).split()
        coe_a = int(str1[0])
        coe_b = int(str1[1])
        coe_c = int(str1[2])
        discr = coe_b^2 - 4 * coe_a * coe_c
        bot.send_message(message.chat.id, f'Дискриминант равен {discr}')
        if discr > 0:
            bot.send_message(message.chat.id, f'У уравнения два корня:\n\
            Первый корень: {round(-coe_b + abs(discr)/(2 * coe_a), 1)}\n\
            Второй корень: {round(-coe_b - abs(discr)/(2 * coe_a), 1)}')
        elif discr == 0:
            bot.send_message(message.chat.id, f'У уравнения один корень: \
            {round(-coe_b/(2 * coe_a), 1)}')
        else:
            bot.send_message(message.chat.id, 'У уравнения нет решений')
    else:
        bot.reply_to(message, 'Не правильно введены коэффициенты')
        register(message)


bot.polling(none_stop=True)