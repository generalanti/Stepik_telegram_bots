"""Здесь представлены сниппеты для телеграм бота. Они записаны по ходу обучения на stepik"""
import telebot
bot = telebot.TeleBot(1352456453)


""" Проверка в хэндлерах работает сверху вниз, и если хоть какой то хэндлер проходит проверку,
 то другие не будут проверяться"""

"""Для отладки"""

# Если введены команды из списка, то выдаст полную инфу о чате, пользователе и т.д.
@bot.message_handler(commands=['start', 'end'])
def start(message):
    bot.send_message(message.chat.id, message)


"""Как бот может отвечать"""

# Меняем получателя всех писем
@bot.message_handler(commands=['start', 'end'])
def start(message):
    bot.send_message(316075399, 'Hi!')


"""Фильтры обработчиков"""

# Ответ в зависимости от введенной команды
@bot.message_handler(commands=['start', 'end'])
def start(message):
    bot.send_message(message.chat.id, 'Hi!')

# Ответ в зависимости от типа чата
@bot.message_handler(chat_types=['private'])
def start(message):
    bot.send_message(message.chat.id, 'Hi!')

# Ответ в зависимости от типа контента
@bot.message_handler(content_types=['photo', 'video'])
def start(message):
    bot.send_message(message.chat.id, 'Hi!')

# Ответ в зависимости от регулярки
@bot.message_handler(regexp=r'[0-9]+')
def start(message):
    bot.send_message(message.chat.id, 'Hi!')

# Ответ в зависимости от результата функции
# бот отвечает на конкретные слова (lambda)
@bot.message_handler(func=lambda message: message.text == '1')
def start(message):
    bot.reply_to(message, 'Hi!')

# бот отвечает на все слова (lambda)
@bot.message_handler(func=lambda message: True)
def start(message):
    bot.reply_to(message, 'Hi!')

# Либо без lambda
def f(message):
    return message.text == '1'

@bot.message_handler(func=f)
def start(message):
    bot.reply_to(message, 'Hi!')







bot.polling(none_stop=True)


