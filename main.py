# our bot's ID silver_rare_fish_bot
import telebot
from sentence_determinant import SentenceDeterminant
import datetime
from faq import current_time


def log():
    logg = open('all.log', 'a')
    logg.write('\n')
    logg.close()


# our bots token:
token = '6054282792:AAG3MKRoB_31Nn39kMBQHhIGHbaEdGo_FJg'

# initialize
bot = telebot.TeleBot(token)
sen_det = SentenceDeterminant()


# here is example, where bot will reply to comand 'start' to the chat, from where he was texted fraze
@bot.message_handler(commands=['start'])
def start_message(message):
    log = open('logs/all.log', 'a')

    bot.send_message(message.chat.id, 'hello there')
    log.write(f'new user, chat id = {message.chat.id}\n')
    log.close()


@bot.message_handler(commands=['time'])
def ret_sum(message):
    bot.send_message(message.chat.id, datetime.datetime.now())


# I don't understand it completely, but bot will reply to anything with same text
@bot.message_handler(func=lambda message: True)
def irritate(message):
    if (sen_det.get_closest_question(message.text) is current_time):
        func = sen_det.get_closest_question(message.text)
        bot.reply_to(message, func())
    else:
        bot.reply_to(message, sen_det.get_closest_question(message.text))


bot.infinity_polling()
