# our bot's ID silver_rare_fish_bot
import telebot

# our bot's token:
token = '6054282792:AAG3MKRoB_31Nn39kMBQHhIGHbaEdGo_FJg'

# initialize bot
bot = telebot.TeleBot(token)

# here is example, where bot will reply to comand 'start' to the chat, from where he was texted fraze
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello my dear friend. I am really smart bot and if you write me something inappropriate, i would kill you:)')
    print('ALERT')

@bot.message_handler(commands=['sum'])
def ret_sum(message):
    data = message.text
    if len(data) > 6:
        data = data.split(' ')
        ret = int(data[1]) + int(data[2])
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
    bot.reply_to(message, message.text + '\nhehe')

bot.infinity_polling()
