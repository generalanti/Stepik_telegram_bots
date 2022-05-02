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

# Логическое И
# Функция выполнится если все проверки вернут True
# В примере снизу функция будет вызвана если тип сообщения будет текст, и текст сообщения будет 1
@bot.message_handler(content_types = ['text'], func = lambda message: message.text == '1')
def send_something(message):
    pass


# Логическое ИЛИ
# Функция выполнится если хотя бы один из обработчиков пройдёт проверку.
# В примере снизу функция будет вызвана если текст сообщения будет 1 или будет использована команда /hello
@bot.message_handler(func = lambda message: message.text == '1')
@bot.message_handler(commands=['hello'])
def send_something(message):
    pass


# Бот отправляет фото
@bot.message_handler(commands=['start', 'end'])
def start(message):
    file = open('photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file)

# Бот отправляет видео
@bot.message_handler(commands=['start', 'end'])
def start(message):
    file = open('video.mp4', 'rb')
    bot.send_video(message.chat.id, file)

# Команды для других типов
bot.send_audio(chat_id, audio)  # аудио
bot.send_voice(chat_id, voice)  # голосовое сообщение
bot.send_document(chat_id, doc) # документ
bot.send_sticker(chat_id, "sticker_id") # стикер

# Бот отправляет фото и сообщение
@bot.message_handler(commands=['start', 'end'])
def start(message):
    file = open('photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Это фото')

# Бот отправляет фото с онлайн ресурса
@bot.message_handler(commands=['start', 'end'])
def start(message):
    bot.send_photo(message.chat.id, r'https://c.tenor.com/JR6q0Nvzr_wAAAAC/baby-yoda.gif')

# Бот получает фото и отправляет такое же обратно по id
# для других типов контента, bot.send_message(message.chat.id, message)
@bot.message_handler(content_types=['photo'])
def start(message):
    bot.send_photo(message.chat.id, message.photo[0].file_id)


# Форматирование текста
@bot.message_handler(func=lambda m: True)
def chat(message):
    bot.send_message(message.chat.id, '_любой_ текст', parse_mode='Markdown')   # курсив, с помощью Markdown
    bot.send_message(message.chat.id, '<b>любой</b> текст', parse_mode='HTML')      # Жирный, с помощью HTML
# Рекомендуется использовать  HTML, так как он остается неизменным с обновлениями библиотеки



# Получаем id сообщения самого бота
@bot.message_handler(commands=['start'])
def start(message):
    message1 = bot.send_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, message1.id)


# Удаляем сообщение
@bot.message_handler(func=lambda message: True)
def start(message):
    bot.delete_message(message.chat.id, message.id)

# Удаляем сообщение самого бота
    m1 = bot.send_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, m1.id)

# Редактируем сообщение бота
bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text='Какой-то текст', parse_mode='HTML', reply_markup=keyboard)

# добавление кнопок из ReplyKeyboardMarkup
@bot.message_handler(content_types=['text'])
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Catalog = types.KeyboardButton(text="Каталог")
    Info = types.KeyboardButton(text="Информация")
    startKBoard.add(Catalog, Info)
    bot.send_message(message.chat.id, "Добро пожаловать в магазин цифровых товаров", reply_markup=startKBoard)





# заставляет бота работать в цикле
bot.polling(none_stop=True)


