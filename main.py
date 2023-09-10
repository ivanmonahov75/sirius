# our bot's ID silver_rare_fish_bot
import telebot

# our bot's token:
token = '6054282792:AAG3MKRoB_31Nn39kMBQHhIGHbaEdGo_FJg'

# initialize bot
bot = telebot.TeleBot(token)

# here is example, where bot will reply to comand 'start' to the chat, from where he was texted fraze
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello there')
    print('ALERT')

# I don't understand it completely, but bot will reply to anything with same text
@bot.message_handler(func=lambda message: True)
def irritate(message):
    bot.reply_to(message, message.text + '\nhehe')

bot.infinity_polling()
