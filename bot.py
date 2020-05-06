import telebot
from telebot import apihelper
import config

apihelper.proxy = {'https':'socks5://96.96.33.133:1080'}
bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Саня', 'Герой4?', 'я тебя люблю')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'дратути! Я - тест-бот, нажмите кнопку, позязя', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'герой4?':
        file = open('FILE.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'саня':
        file1 = open('FILE.mp3', 'rb')
        bot.send_audio(message.chat.id, file1)
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeQl6xMpVMUR7YscxFsPvnkGwPcP4FAALHAAMw1J0RtZ_tS_0N3O4ZBA')

bot.polling()
