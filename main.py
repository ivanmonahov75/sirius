# our bot's ID silver_rare_fish_bot
import telebot
import os
from dotenv import load_dotenv
from sentence_determinant import SentenceDeterminant
import datetime
from faq import current_time


def gen_env_var(var_name):
    load_dotenv()
    return os.getenv(var_name)


def log(_type, mess):  # basal log function
    logg = open('logs/all.log', 'a')
    logg.write(f'{datetime.datetime.now()}, {_type}, {mess}\n')
    logg.close()
    return f'{datetime.datetime.now()}, {_type}, {mess}\n'


def log_new(username, chat_id):
    return log('new user', f'username: {username}, chatID: {chat_id}')


def log_mess(username, chat_id, mess, reply):
    return log('message', f'username: {username}, chatID: {chat_id}, message: "{mess}", reply: "{reply}"')


def log_command(username, chat_id, mess, reply):
    return log('command', f'username: {username}, chatID: {chat_id}, message: "{mess}", reply: "{reply}"')


# our bots token:
token = gen_env_var('TOKEN')

# initialize
bot = telebot.TeleBot(token)
sen_det = SentenceDeterminant()


# here is example, where bot will reply to command 'start' to the chat, from where he was texted fraze
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello there')
    bot.send_message(gen_env_var('OPERATOR'), f'WARNING\n@{message.from_user.username} started talking to bot at {datetime.datetime.now()}')
    print(log_new(message.from_user.username, message.chat.id))


@bot.message_handler(commands=['time'])
def ret_sum(message):
    date = f'Current time is {datetime.datetime.now()}'
    bot.send_message(message.chat.id, date)
    print(log_command(message.from_user.username, message.chat.id, message.text, date))


# I don't understand it completely, but bot will reply to anything with same text
@bot.message_handler(func=lambda message: True)
def irritate(message):
    reply = sen_det.get_closest_question(message.text)

    if reply is None:
        reply = "Я не знаю ответ на вопрос, дождитесь ответа оператора"
        bot.send_message(gen_env_var('OPERATOR'), f'WARNING\nMessage from user @{message.from_user.username}: {message.text}')
    if reply is current_time:
        bot.reply_to(message, current_time())
    else:
        bot.reply_to(message, reply)
    print(log_mess(message.from_user.username, message.chat.id, message.text, reply))
bot.infinity_polling()
