from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from initBot import userStatus
from UI import volunteerRegistration, volunteerResumeRegistration


class FSMvolunteer(StatesGroup):
    fullName = State()
    university = State()
    faculty = State()


# // @dp.message_handler(commands='Волонтёр')
async def volunteer_profile_init(message: types.Message):
    global userStatus
    if not userStatus[-1]:
        userStatus.append(True)
        await message.answer('Определён волонтёр.')
        await FSMvolunteer.fullName.set()
        await message.answer("Введите ваше полное имя(в формате ФИО).", reply_markup=volunteerRegistration)
    else:
        await message.answer('Вы уже выбрали свой статус.')

async def volunteer_profile_name(message: types.Message, state=FSMContext):
    async with state.proxy() as volunteer_profile:
        volunteer_profile['ФИО:'] = message.text
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
    await message.answer("Регистрация завершена.", reply_markup=ReplyKeyboardRemove())
    #TODO Заменить на вывод в БД:
    #< async with state.proxy() as volunteer_profile:
    #<     await message.answer(f"Ваши регистрационные данные: {str(volunteer_profile)}")
    await state.finish()
    #TODO Отправить анкету на верификацию модераторам.
    await message.answer('Ваша заявка принята в обработку.')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None: return
    await state.finish()
    await message.answer('Регистрация отменена.', reply_markup=volunteerResumeRegistration)
    
    
async def resume_registration(message: types.Message):
    await FSMvolunteer.fullName.set()
    await message.answer("Введите ваше полное имя(в формате ФИО).", reply_markup=volunteerRegistration)



def register_volunteer_handlers(dp: Dispatcher):
    dp.register_message_handler(volunteer_profile_init, Text(equals="Волонтёр", ignore_case=True), state=None)
    dp.register_message_handler(cancel_registration, Text(equals="Отмена", ignore_case=True),state="*")
    dp.register_message_handler(volunteer_profile_name, state=FSMvolunteer.fullName)
    dp.register_message_handler(volunteer_profile_university, state=FSMvolunteer.university)
    dp.register_message_handler(volunteer_profile_faculty, state=FSMvolunteer.faculty)
    dp.register_message_handler(resume_registration, Text(equals="Регистрация", ignore_case=True), state=None)
    
