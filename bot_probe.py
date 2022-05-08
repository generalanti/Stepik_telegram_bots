# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types
import random

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDxWITCaZnaUelQ0SNlHMTrjd2klAmAAIBAQACVp29CiK-nw64wuY0IwQ')
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}\n\
Ты зачем сюда пришел?\n\
Наверное хочешь научиться телеграм ботов создавать?')


@bot.message_handler(regexp='Да')
def edit_and_delete_messages(message):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id-1, text='<b>Ты уверен?</b>\n/da\n/net',\
                          parse_mode='HTML')
    bot.delete_message(message.chat.id, message.id)



@bot.message_handler(commands=['net'])
def send_document(message):
    filename = 'tochno.txt'
    core_word = 'Точно?'
    with open(filename, 'w+', encoding='utf-8') as file:
        for line in range(25):
            for word in range(25):
                file.write(f'{core_word} ')
            file.write('\n')
    file = open(filename, 'rb')
    bot.send_message(message.chat.id, 'Ну ладно')
    bot.send_document(message.chat.id, file)


@bot.message_handler(commands=['da'])
def send_document(message):
    k_board = types.InlineKeyboardMarkup(row_width=3)
    btn_1 = types.InlineKeyboardButton(text='Да', callback_data='btn1')
    btn_2 = types.InlineKeyboardButton(text='Нет', callback_data='btn2')
    btn_3 = types.InlineKeyboardButton(text='Нет', callback_data='btn3')
    k_board.add(btn_2, btn_1, btn_3)
    bot.send_message(chat_id=message.chat.id, text='Подумай еще раз', reply_to_message_id=message.id, reply_markup=k_board)

# TODO: доработать механизм шафлинга кнопок (выскакивают ошибки одинаковых последовательностей)
@bot.callback_query_handler(func=lambda c:c.data)
def switch_inline_btns(callback):
    if callback.data in ['btn2', 'btn3']:
        flag = True
        while flag:
            markup = types.InlineKeyboardMarkup(row_width=3)
            btn_1 = types.InlineKeyboardButton(text='Да', callback_data='btn1')
            btn_2 = types.InlineKeyboardButton(text='Нет', callback_data='btn2')
            btn_3 = types.InlineKeyboardButton(text='Нет', callback_data='btn3')
            lst = [btn_1, btn_2, btn_3]
            random.shuffle(lst)
            markup.add(*lst)
            try:
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                      text="Что ты выберешь?", reply_markup=markup)
                flag = False
            except Exception as e:
                flag = True
                print(f'Произошла ошибка: {e}')

    elif callback.data == 'btn1':
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        btn_A = types.InlineKeyboardButton(text='Да', callback_data='btnA')
        btn_B = types.InlineKeyboardButton(text='Нет', callback_data='btnB')
        btn_C = types.InlineKeyboardButton(text='Нет', callback_data='btnC')
        markup2.add(btn_A, btn_B, btn_C)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text="Что ты выберешь?", reply_markup=markup2)
    elif callback.data in ['btnA', 'btnB', 'btnC']:
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        btn_link = types.InlineKeyboardButton(text='Зайди сюда', url='https://7qp.github.io/telegram_bot/')
        markup3.add(btn_link)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text='Хорошо', reply_markup=markup3)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_photo(message.chat.id, r'https://7qp.github.io/telegram_bot/img/photo.jpg')

    sent = bot.send_message(message.chat.id, 'Введи свое имя в телеграме')
    bot.register_next_step_handler(sent, user_id_check)

def user_id_check(message):
    if message.from_user.id == message.text:
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Добро пожаловать!', url='https://7qp.github.io/telegram_bot/')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, 'ссылка', reply_markup=markup)





# @bot.message_handler(func=lambda message: message.text == 'Решить квадратное уравнение')
# def register(message):
#     sent = bot.reply_to(message, 'Введите коэффициенты ax^2 + bx + c в виде: a b c')
#     bot.register_next_step_handler(sent, calc)
#
#
# def calc(message):
#     str1 = message.text
#     result = re.search(r'-?\d+\s-?\d+\s-?\d+', str1)
#     if result:
#         bot.send_message(message.chat.id, 'Коэффициенты введены верно, начинаю решать уравнение')
#         str1 = result.group(0).split()
#         coe_a = int(str1[0])
#         coe_b = int(str1[1])
#         coe_c = int(str1[2])
#         discr = coe_b ** 2 - 4 * coe_a * coe_c
#         bot.send_message(message.chat.id, f'Дискриминант равен {discr}')
#         if discr > 0:
#             bot.send_message(message.chat.id, f'У уравнения два корня:\n\
#             Первый корень: {round(- coe_b + discr ** (0.5)/(2 * coe_a), 3)}\n\
#             Второй корень: {round(- coe_b - discr ** (0.5)/(2 * coe_a), 3)}')
#         elif discr == 0:
#             bot.send_message(message.chat.id, f'У уравнения один корень: {round(-coe_b/(2 * coe_a), 1)}')
#         else:
#             bot.send_message(message.chat.id, 'У уравнения нет решений')
#     else:
#         bot.reply_to(message, 'Не правильно введены коэффициенты')
#         register(message)


bot.polling(none_stop=True)