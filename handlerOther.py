from aiogram import types, Dispatcher
from initBot import running
from UI import statusDefiningButtons


# // @dp.message_handler(commands=['start', 'help'])
async def first_interaction(message: types.Message):
    '''On start-button press.'''
    global running
    if not running[-1]:
        await message.answer('Добро пожаловать в сервис Коннект. Пожалуйста, определите ваш статус.', reply_markup=statusDefiningButtons)
        running.append(True)
    else:
        await message.answer('Вы уже начали взаимодействие с ботом.')


# // @dp.message_handler()
async def other_messages(message: types.Message):
    await message.answer('Пока что бот вас не понимает.')


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(first_interaction, commands=['start', 'help'])
    dp.register_message_handler(other_messages)
