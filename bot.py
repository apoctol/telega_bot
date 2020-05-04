import telebot

bot = telebot.TeleBot('1227798458:AAGQv64o2Qp4nENCw5rxo1Dhp6VeyzhqWEo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
