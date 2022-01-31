#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- dialog params -------------------
dialog = {
    'shisha': {
        'in': ['кальян', 'калюсік', 'коля', 'нікалай'],
        'out': ['О, сьогодні курим?']
    },
    'shisha_soft': {
        'in': ['табак', 'табаки', 'табачки', 'углі', 'вугілля', 'табачок'],
        'out': ['Кальян визиває базу']
    },
    'igor': {
        'in': ['ігор', 'ігарьок'],
        'out': ['О, Ігарьок', 'Ігарьок, го на пиво?', 'По пивку?', 'Ііігаарь', 'Не Ігарь а Гіга', 'О, Ігарьок,покорми оскара']
    },
    'mishka': {
        'in': ['міша', 'мішка'],
        'out': ['Міша-Маваши', 'Міша-Лавашик','Сам ти Мішка', 'Мішка клин клином', 'Мішка хуй', 'А шо зразу Мішка?', 'Мішка? Романи бивший?', 'Мішка метр з кэпкой', 'Мішка-хуїшка']
    },
    'pivas': {
        'in': ['пиво', 'півас', 'півасік', 'лучан', 'акцент', 'кєга', 'кега', 'бакал', 'бокал', 'бакальчик', 'бакальчику'],
        'out': ['Алкаш.', 'Алкашка.', 'Алкаши.', 'оооо бухіч!!!', 'а може шо покрєпчє?', 'го', 'я за', 'сам пий, хуй']
    },
    'tsypah': {
        'in': ['цюпах', 'цюпях'],
        'out': ['цюпах-хуюпах']
    },
    'tsypah2': {
        'in': ['цюпашня', 'цюпашняшка'],
        'out': ['цюпашня-хуяшня']
    },
    'narod': {
        'in': ['народ'],
        'out': ['Народ - хуй тобі в рот']
    },
    'narod2': {
        'in': ['рібята', 'рєбята'],
        'out': ['Рібята - Тірібята']
    },
    'hi': {
        'in': ['привіт', 'прівєт', 'хай'],
        'out': ['Шо хоч?']
    },
    'typo1': {
        'in': ['маїш'],
        'out': ['*маєш']
    },
    'typo2': {
        'in': ['хочиш'],
        'out': ['*хочеш']
    },
    'typo3': {
        'in': ['будиш'],
        'out': ['*будеш']
    },
    'typo4': {
        'in': ['будиш'],
        'out': ['*будеш']
    },
    'hello': {
        'in': ['альо', 'ало'],
        'out': ['альо-альо, я на связі?']
    },
    'home': {
        'in': ['по домам', 'вдома'],
        'out': ['ха-ха, домосєди']
    },
    'pass': {
        'in': ['пас', 'пасс'],
        'out': ['хуяс.']
    },
    'antonio': {
        'in': ['антон', 'антошка', 'антоніна'],
        'out': ['Антошка-хуйошка', 'Всмислі?', 'Антошка, як там твоя коллекція бутилочок? Добре? Запхай їх собі в дупу.']
    },
    'happy': {
        'in': ['вітаю', 'вітаємо', 'приєднуюсь', 'хепі', 'хеппі', 'деньчік', 'деньчіком'],
        'out': ['Вітаємо']
    },
    'g1': {
        'in': ['мед', 'горіх', 'горіхи', 'цукерки', 'шоколад', 'шоколадка', 'пилюка', 'цвіт'],
        'out': ['В Журвальова на це алергія.']
    },
    'g2': {
        'in': ['журавльов'],
        'out': ['Журвальов + алергія = Монгол']
    },
    'p1': {
        'in': ['Петлюрику', 'Петлюрику?'],
        'out': ['Петлюрик-хуюрик.']
    },
    'l1': {
        'in': ['лавнічек', 'лавнічек'],
        'out': ['Лавнічек, де права згубив?']
    }
}


# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Hello! This is a telegram bot template written by <a href="https://github.com/otter18">otter18</a></b>',
        parse_mode='html'
    )


@bot.message_handler(func=lambda message: True)
def echo(message):
    for t, resp in dialog.items():
        if sum([e in message.text.lower() for e in resp['in']]):
            logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used {t}:\n\n%s', message.text)
            bot.send_message(message.chat.id, random.choice(resp['out']))
            return

    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used echo:\n\n%s', message.text)


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
