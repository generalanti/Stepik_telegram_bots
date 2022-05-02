# --*-- encoding: utf-8 --*--

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['buy'])
def chat(message):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id - 1, text='modified',\
                          parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def bot_chat(message):
    bot.send_message(message.chat.id, f'bot message: {message.id}')




bot.polling(none_stop=True)