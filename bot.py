# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    with open('file.txt', 'w+', encoding='utf-8') as file:
        file.write(f'{message.text}')
    doc = open('file.txt', 'rb')
    bot.send_document(message.chat.id, doc)




bot.polling(none_stop=True)
