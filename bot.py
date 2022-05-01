# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['sticker'])
def start(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

bot.polling(none_stop=True)
