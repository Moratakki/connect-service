from aiogram import types, Dispatcher
from initBot import dp, bot, running, status
import json
import string


# // @dp.message_handler(commands=['start', 'help'])
async def first_interaction(message: types.Message):
    '''On start-button press.'''
    global running
    if not running:
        await message.answer('Добро пожаловать в сервис Коннект.')
    else:
        await message.answer('Вы уже начали взаимодействие с ботом.')
    running = True


# // @dp.message_handler(commands='Абитуриент')
async def applicant_init(message: types.Message):
    global status
    if not status:
        await message.answer('Определён абитуриент.')
        #! have to initialize registration
    else:
        await message.answer('Вы уже выбрали свой статус')
    status = True


# // @dp.message_handler(commands='Волонтёр')
async def volunteer_init(message: types.Message):
    global status
    if not status:
        await message.answer('Определён волонтёр.')
        #! have to initialize registration
    else:
        await message.answer('Вы уже выбрали свой статус.')
    status = True


# // @dp.message_handler()
async def other_messages(message: types.Message):
    if {word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split(' ')}\
            .intersection(set(json.load(open('swears.json')))) != set():
        await message.reply('Пожалуйста, будьте корректнее.')
        await message.delete()
    else:
        await message.answer('Пока что бот вас не понимает.')


'''===================================| HANDLERS REGISTER |==================================='''


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(first_interaction, commands=['start', 'help'])
    dp.register_message_handler(applicant_init, commands=['Абитуриент'])
    dp.register_message_handler(volunteer_init, commands=['Волонтёр'])
    dp.register_message_handler(other_messages)
