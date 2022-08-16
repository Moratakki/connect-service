from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from initBot import userStatus


# // @dp.message_handler(commands='Абитуриент')
async def applicant_init(message: types.Message):
    global userStatus
    if not userStatus[-1]:
        await message.answer('Определён абитуриент.')
        #! have to initialize registration
        userStatus.append(True)
    else:
        await message.answer('Вы уже выбрали свой статус')


def register_applicant_handlers(dp: Dispatcher):
    dp.register_message_handler(applicant_init, Text(equals="Абитуриент", ignore_case=True))
