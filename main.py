#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- dialog params -------------------
reply = {
    'whopirate': {
        'in': ['хто пірат', 'хто пірат?', 'хто на вахті', 'хто на вахті?'],
        'out': [
            'Саша Цюпях',
            'Юля Лавнічек',
            'Діма Лавнічек',
            'Діма Журавльов',
            'Ігор Никитюк',
            'Настя Никитюк',
            'Оля Голячук',
            'Софа Бичковська',
            'Юля Акерман',
            'Саша Акерман',
            'Олена Цалко',
            'Антон Цалко'
        ]
    }
}

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
        'out': ['Ігарьок, скільки разів підтягнешся?', 'О, Ігарьок', 'Ігарьок, го на пиво?', 'По пивку?', 'Ііігаарь', 'Не Ігарь а Гіга', 'О, Ігарьок,покорми оскара']
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
        'out': ['Прівєт.', 'Хай.']
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
        'out': ['Антошка-хуйошка', 'Всмислі?', 'Антошка, як там твоя коллекція бутилочок?']
    },
    'happy': {
        'in': ['вітаю', 'вітаємо', 'приєднуюсь', 'хепі', 'хеппі', 'деньчік', 'деньчіком'],
        'out': ['Вітаємо']
    },
    'g1': {
        'in': ['мед', 'горіх', 'горіхи', 'цукерки', 'шоколад', 'шоколадка', 'пилюка', 'цвіт', 'оса', 'оси', 'бджола', 'бджоли'],
        'out': ['В Журавальова на це алергія.']
    },
    'g2': {
        'in': ['журавльов'],
        'out': ['Журавальов + алергія = Монгол']
    },
    'petl1': {
        'in': ['Петлюрику', 'Петлюрику?', 'Петлюрик'],
        'out': ['Петлюрик-хуюрик.']
    },
    'lovenicheck1': {
        'in': ['лавнічек', 'лавнічек'],
        'out': ['Лавнічек, де права згубив?']
    },
    'football1': {
        'in': ['футбік', 'футбол'],
        'out': ['Футбол для лохів']
    },
    'volyn1': {
        'in': ['волинь', 'динамо', 'гра'],
        'out': ['Волинь - чемпіон!']
    },
    'olga1': {
        'in': ['оля', 'олька', 'голячук'],
        'out': ['Олька, коли в луцьк?']
    },
    'go': {
        'in': ['парк', 'гуляти'],
        'out': ['нє, не піду, погодка гавно']
    },
    'go2': {
        'in': ['погода', 'погодка'],
        'out': ['погодка пітьєва']
    },
    'kolyba': {
        'in': ['колиба', 'колибу', 'колибі', 'степова', 'степову', 'степовій'],
        'out': ['Знову в колибу на степовій?']
    },
    '3sta': {
        'in': ['триста', ' 300 '],
        'out': ['Відсоси у тракториста']
    },
    '3sta': {
        'in': ['триста', ' 300 '],
        'out': ['Відсоси у тракториста']
    },
    'valentin': {
        'in': ['валентина', 'валентин', '14 лютого'],
        'out': ['знов Лєна нап\'ється?']
    },
    'ga': {
        'in': ['прапор'],
        'out': ['🏳️‍🌈']
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
    for t, resp in reply.items():
        if sum([e in message.text.lower() for e in resp['in']]):
            logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used {t}:\n\n%s', message.text)
            bot.reply_to(message, random.choice(resp['out']))
            return

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
