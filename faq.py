import datetime
from time import *
QUESTIONS = {
    'Какая погода?': 1,
    'Что сегодня за окном?': 1,
    'Что говорит метеостанция?': 1,
    'Как дойти до столовки?': 2,
    'как купить картошку': 3,
    'где купить картофель': 3,
    'как ботать всош': 4,
    'как получить диплом': 4,
    'который сейчас час': 5,
    'сколько время': 5
}
def current_time():
    return datetime.datetime.now()

ANSWERS = {
    1: 'Сегодня солнечно',
    2: 'В четверг налево',
    3: 'На рынке купишь свою картошку',
    4: 'тяжело его заботать',
    5: current_time
}