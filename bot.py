# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['video', 'photo'])
@bot.message_handler(commands=['start'])
def start(message):
    if message.content_type == 'photo':
        bot.send_photo(5167752966, message.photo[0].file_id)
    elif message.content_type == 'video':
        bot.send_video(5167752966, message.video.file_id)


@bot.message_handler(func=lambda m: True)
def chat(message):
    bot.send_message(5167752966, 'Это не видео и не фото :(')

bot.polling(none_stop=True)
