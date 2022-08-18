from aiogram import types, Dispatcher
import initBot
from userButtons import statusDefiningButtons


# // @dp.message_handler(commands=['start', 'help'])
async def first_interaction(message: types.Message):
    await message.answer('Добро пожаловать в сервис Коннект. Пожалуйста, определите ваш статус.', reply_markup=statusDefiningButtons)


# // @dp.message_handler()
async def other_messages(message: types.Message):
    await message.answer('Пока что бот вас не понимает.')


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(first_interaction, commands=['start', 'help'])
    dp.register_message_handler(other_messages)