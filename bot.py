# --*-- encoding: utf-8 --*--

import config
import telebot

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'location', 'contact'])
def start(message):
    out_messages_ru = {'text': 'Это текст', 'audio': 'Это аудио', 'document': 'Это документ', 'photo': 'Это фото',
                       'sticker': 'Это стикер', 'video': 'Это видео', 'location': 'Это геопозиция', 'contact': 'Это контакт'}
    bot.send_message(message.chat.id, out_messages_ru[message.content_type])


bot.polling(none_stop=True)
