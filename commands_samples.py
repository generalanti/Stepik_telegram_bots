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
bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text='Какой-то текст', parse_mode='HTML', reply_markup='keyboard')

# добавление кнопок из ReplyKeyboardMarkup
@bot.message_handler(content_types=['text'])
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Catalog = types.KeyboardButton(text="Каталог")
    Info = types.KeyboardButton(text="Информация")
    startKBoard.add(Catalog, Info)
    bot.send_message(message.chat.id, "Добро пожаловать в магазин цифровых товаров", reply_markup=startKBoard)


# Убираем клавиатуру
bot.send_message(message.chat.id, "Убираем клавиатуру", reply_markup=types.ReplyKeyboardRemove())

# чтобы клавиатура исчезла при нажатии кнопки
kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)

# добавление кнопок из InlineKeyboardMarkup
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://stepik.org/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

# добавление switch-кнопки (с последующей активацией бота в другом чате в inline режиме)
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)


# Callback кнопки =)
@bot.message_handler(commands=['start'])
def cmd_start(message):
    start_keyboard = types.InlineKeyboardMarkup()
    Hack_Pentagon = types.InlineKeyboardButton(text='Hack Pentagon', callback_data='HackPentagon')
    Snorovka_School = types.InlineKeyboardButton(text='Snorovka School', callback_data='SnorovkaSchool')
    start_keyboard.add(Hack_Pentagon, Snorovka_School)
    bot.send_message(message.chat.id, 'А вот и callback кнопки!', reply_markup=start_keyboard)
    # Или если нужно ответить (reply) с кнопками:
    bot.send_message(chat_id=message.chat.id, text='А вот и callback кнопки!', \
                     reply_to_message_id=message.id, reply_markup=start_keyboard)


#Если получаем callback ответ с клавиатуры запускаем функцию answer_callback
@bot.callback_query_handler(func=lambda c:c.data)
def answer_callback(callback):
    if callback.data == 'SnorovkaSchool':
        #Что-то делаем
    elif callback.data == 'HackPentagon':
        #Взламываем Пентагон


# изменяем ранее сделанные кнопки (по факту меняем клавиатуру)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Какой-то текст',
                              reply_markup=some_keyboard)

# Отправка больших сообщений (разбиение больших сообщений на более мелкие)
from telebot import util
large_text = open("large_text.txt", "rb").read()

# Разбивает одну строку на несколько строк с максимальным количеством `символов на строку` (макс. 4096)
# Разбиение происходит на '\n', '.' или ' ' именно с таким приоритетом.
# smart_split возвращает список с разделенным текстом.

splitted_text = util.smart_split(large_text, chars_per_string=3000)
for text in splitted_text:
	bot.send_message(chat_id, text)


# получение текста сообщения пользователя в python
@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.reply_to(message, 'Пожалуйста, оставьте отзыв!')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    message_to_save = message.text
    #message.text и будет являться пользовательским вводом
    #Теперь мы можем делать с ним всё, что захотим
    bot.send_message(message.chat.id, 'Спасибо!')





# заставляет бота работать в цикле
bot.polling(none_stop=True)


