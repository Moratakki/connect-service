from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from userModerating import volunteer_confirmation
import initBot
from userButtons import volunteerRegistration, volunteerResumeRegistration



class FSMvolunteer(StatesGroup):
    fullName = State()
    city = State()
    university = State()
    faculty = State()


async def volunteer_profile_init(message: types.Message):
    inApplicantsDatabase = initBot.crsr.execute("SELECT TelegramID FROM applicants WHERE TelegramID = {}".format(message.from_user.id)).fetchone()
    inVolunteersDatabase = initBot.crsr.execute("SELECT TelegramID FROM volunteers WHERE TelegramID = {}".format(message.from_user.id)).fetchone()
    
    if inApplicantsDatabase or inVolunteersDatabase:
        await message.answer('Вы не можете переопределить свой статус, так как уже находитесь в базе.')
    else:
        await message.answer('Определён волонтёр.')
        await FSMvolunteer.fullName.set()
        await message.answer("Введите ваше полное имя(в формате ФИО).", reply_markup=volunteerRegistration)

async def volunteer_profile_name(message: types.Message, state=FSMContext):
    async with state.proxy() as volunteer_profile:
        volunteer_profile['Telegram ID'] = message.from_user.id
        volunteer_profile['Telegram Username'] = message.from_user.username
        volunteer_profile['ФИО'] = message.text
    await FSMvolunteer.next()
    await message.answer("Введите название города, в котором расположен ваш ВУЗ.")
    
async def volunteer_profile_city(message: types.Message, state=FSMContext):
    async with state.proxy() as volunteer_profile:
        volunteer_profile['Город'] = message.text
    await FSMvolunteer.next()
    await message.answer("Введите название ВУЗа, в котором вы обучаетесь.")    

async def volunteer_profile_university(message: types.Message, state=FSMContext):
    async with state.proxy() as volunteer_profile:
        volunteer_profile['ВУЗ'] = message.text
    await FSMvolunteer.next()
    await message.answer("Введите название вашего факультета.")

async def volunteer_profile_faculty(message: types.Message, state=FSMContext):
    async with state.proxy() as volunteer_profile:
        volunteer_profile['Факультет'] = message.text
        volunteer_profile['Подтверждён'] = 0
    await message.answer("Регистрация завершена.", reply_markup=ReplyKeyboardRemove())
    async with state.proxy() as volunteer_profile:
        initBot.crsr.execute("INSERT INTO volunteers VALUES(?, ?, ?, ?, ?, ?, ?)", tuple(volunteer_profile.values()))
        initBot.userDB.commit()
        volunteerData = initBot.crsr.execute("SELECT * FROM {}  WHERE TelegramID = {}".format('volunteers', volunteer_profile['Telegram ID'])).fetchone()
        volunteerRowId = initBot.crsr.execute("SELECT rowid FROM {}  WHERE TelegramID = {}".format('volunteers', volunteer_profile['Telegram ID'])).fetchone()[0]
    await volunteer_confirmation(volunteerData, volunteerRowId)
    await state.finish()
    await message.answer('Ваша заявка принята в обработку.')



async def cancel_registration(message: types.Message, state: FSMContext):
    if await state.get_state() is None: return
    await state.finish()
    await message.answer('Регистрация отменена.', reply_markup=volunteerResumeRegistration)
     
async def resume_registration(message: types.Message):
    await FSMvolunteer.fullName.set()
    await message.answer("Введите ваше полное имя(в формате ФИО).", reply_markup=volunteerRegistration)



async def declined_request_notice(vlnt_id):
    await initBot.bot.send_message(vlnt_id, 'Ваша заявка была отклонена.')
        
async def accepted_request_notice(vlnt_id):
    await initBot.bot.send_message(vlnt_id, 'Ваша заявка была принята.')





def register_volunteer_handlers(dp: Dispatcher):
    dp.register_message_handler(volunteer_profile_init, Text(equals="Волонтёр", ignore_case=True), state=None)
    dp.register_message_handler(cancel_registration, Text(equals="Отмена", ignore_case=True),state="*")
    dp.register_message_handler(volunteer_profile_name, state=FSMvolunteer.fullName)
    dp.register_message_handler(volunteer_profile_city, state=FSMvolunteer.city)
    dp.register_message_handler(volunteer_profile_university, state=FSMvolunteer.university)
    dp.register_message_handler(volunteer_profile_faculty, state=FSMvolunteer.faculty)
    dp.register_message_handler(resume_registration, Text(equals="Регистрация", ignore_case=True), state=None)