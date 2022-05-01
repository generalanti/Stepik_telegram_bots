# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def chat(message):
    bot.delete_message(message.chat.id, message.id)
    m1 = bot.send_message(message.chat.id, 'Я удалил твое сообщение')
    bot.delete_message(message.chat.id, m1.id)



bot.polling(none_stop=True)