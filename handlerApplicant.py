from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import initBot



# // @dp.message_handler(commands='Абитуриент')
async def applicant_init(message: types.Message):
    inApplicantsDatabase = initBot.crsr.execute("SELECT TelegramID FROM applicants WHERE TelegramID = {}".format(message.from_user.id)).fetchone()
    inVolunteersDatabase = initBot.crsr.execute("SELECT TelegramID FROM volunteers WHERE TelegramID = {}".format(message.from_user.id)).fetchone()
    if inApplicantsDatabase or inVolunteersDatabase:
        await message.answer('Вы не можете переопределить свой статус, так как уже находитесь в базе.')
    else:
        await message.answer('Определён абитуриент.')
    #! have to initialize registration


def register_applicant_handlers(dp: Dispatcher):
    dp.register_message_handler(applicant_init, Text(equals="Абитуриент", ignore_case=True))
