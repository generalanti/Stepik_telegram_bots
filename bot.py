# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda m: True)
def chat(message):
    text = 'Смотри что могу!\n\n<b>Жирный</b>\n<i>Курсив</i>\n<u>Нижнее почеркивание</u>\n<s>Зачеркнутый</s>' \
           '<a href="https://stepik.org/lesson/666879/step/5?auth=login&unit=664880">Гиперссылка</a>'
    bot.send_message(message.chat.id, text, parse_mode='HTML')



bot.polling(none_stop=True)