# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda m: True)
def start(message):
    file = open('saitama.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Я научился писать телеграм ботов тут - https://stepik.org/course/107302/ , а ты что сделал, а? А ну иди делом займись!')

bot.polling(none_stop=True)
