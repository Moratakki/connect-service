from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import json
import string

'''==================================================| INITIALIZING |=================================================='''


bot = Bot(token="5513945226:AAGqopdbfAxZXqAkacz27igq7KvrTISQpFw")
dp = Dispatcher(bot)
running = False
status = False


async def on_startup(_):
    print('\n>>>>>| Bot lauched succesfully. |<<<<<\n')


async def on_shutdown(_):
    print('\n>>>>>| Bot has been shuted down. |<<<<<\n')


'''====================================================| USER-SIDE |===================================================='''


@dp.message_handler(commands=['start', 'help'])
async def first_interaction(message: types.Message):
    '''On start-button press.'''
    global running
    if not running:
        await message.answer('Добро пожаловать в сервис Коннект.')
    else:
        await message.answer('Вы уже начали взаимодействие с ботом.')
    running = True


@dp.message_handler(commands='Абитуриент')
async def applicant_init(message: types.Message):
    global status
    if not status:
        await message.answer('Определён абитуриент.')
        #! have to initialize registration
    else:
        await message.answer('Вы уже выбрали свой статус')
    status = True


@dp.message_handler(commands='Волонтёр')
async def volunteer(message: types.Message):
    global status
    if not status:
        await message.answer('Определён волонтёр.')
        #! have to initialize registration
    else:
        await message.answer('Вы уже выбрали свой статус.')
    status = True


@dp.message_handler()
async def other_messages(message: types.Message):
    if {word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split(' ')}\
            .intersection(set(json.load(open('swears.json')))) != set():
        await message.reply('Пожалуйста, будьте корректнее.')
        await message.delete()
    else:
        await message.answer('Пока что бот вас не понимает.')


'''====================================================| LAUNCH |===================================================='''


executor.start_polling(dp, skip_updates=True,
                       on_startup=on_startup, on_shutdown=on_shutdown)
