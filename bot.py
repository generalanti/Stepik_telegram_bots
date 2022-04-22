# --*-- encoding: utf-8 --*--
# name: GOBfoGpsOgFv_bot

import config
import telebot
import datetime

bot = telebot.TeleBot(config.TOKEN)





@bot.message_handler(content_types=["text"])
def speak(message):
    date = message.date + 10800
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    message_text = message.text

    msg = f"Я пробил информацию:\n\nId чата: {chat_id}\nId пользователя: {user_id}\nИмя: {name}\nФамилия: {lastname}\nПсевдоним: {username}\n\nТекст сообщения: {message_text}"
    msg2 = datetime.datetime.utcfromtimestamp(date)

    bot.send_message(message.chat.id, msg2)


bot.polling(none_stop=True)



