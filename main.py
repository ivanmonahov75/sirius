# our bot's ID silver_rare_fish_bot
import telebot
from sentence_determinant import SentenceDeterminant
import datetime
from faq import current_time
# our bot's token:
token = '6054282792:AAG3MKRoB_31Nn39kMBQHhIGHbaEdGo_FJg'

# initialize
bot = telebot.TeleBot(token)
sen_det = SentenceDeterminant()

# here is example, where bot will reply to comand 'start' to the chat, from where he was texted fraze
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello my dear friend. I am really smart bot and if you write me something inappropriate, i would kill you:)')
    print('ALERT')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
#@bot.message_handler(content_types='text')
#def message_reply(message):
#    if message.text=="Кнопка":
#        data = message.text
#        bot.send_message(message.chat.id, int(data[1])-int(data[2]))


@bot.message_handler(commands=['time'])
def ret_sum(message):
    data = message.text
    if len(data) > 6:
        data = data.split(' ')
        ret = int(data[1]) - int(data[2])
        bot.send_message(message.chat.id, str(ret))
    else:
        bot.send_message(message.chat.id, 'BAD USER')

@bot.message_handler(commands=['dif'])
def ret_sum(message):
    data = message.text
    if len(data) > 6:
        data = data.split(' ')
        ret = int(data[1]) - int(data[2])
        bot.send_message(message.chat.id, str(ret))
    else:
        bot.send_message(message.chat.id, 'BAD USER')

# I don't understand it completely, but bot will reply to anything with same text
@bot.message_handler(func=lambda message: True)
def irritate(message):
    if (sen_det.get_closest_question(message.text) is current_time):
        func = sen_det.get_closest_question(message.text)
        bot.reply_to(message, func())
    else:
        bot.reply_to(message, sen_det.get_closest_question(message.text))

bot.infinity_polling()


