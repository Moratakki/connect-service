from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from initBot import userStatus


# // @dp.message_handler(commands='Волонтёр')
async def volunteer_init(message: types.Message):
    global userStatus
    if not userStatus[-1]:
        await message.answer('Определён волонтёр.', reply_markup=ReplyKeyboardRemove())
        #! have to initialize registration
        userStatus.append(True)
    else:
        await message.answer('Вы уже выбрали свой статус.')


def register_volunteer_handlers(dp: Dispatcher):
    dp.register_message_handler(volunteer_init, commands=['Волонтёр'])
