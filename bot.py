# --*-- encoding: utf-8 --*--

import config
import telebot
import emoji

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["text"])
def speak(message):

    message_text = message.text + '... Ну и на кой хер ты это пишешь? Пожри-ка дерьма ' + emoji.emojize(':shit::shit::shit:', language='alias')

    bot.send_message(message.chat.id, message_text)


bot.polling(none_stop=True)
