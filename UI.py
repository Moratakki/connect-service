from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

applicantInitButton = KeyboardButton("/Абитуриент")
volunteerInitButton = KeyboardButton("/Волонтёр")

statusDefiningButtons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)

statusDefiningButtons.row(applicantInitButton, volunteerInitButton)


volunteerCancelRegistrationButton = KeyboardButton("/Отмена")

volunteerRegistration = ReplyKeyboardMarkup(resize_keyboard=True)
volunteerRegistration.add(volunteerCancelRegistrationButton)


volunteerRegistrationButton = KeyboardButton("/Регистрация")
volunteerResumeRegistration = ReplyKeyboardMarkup(resize_keyboard=True)
volunteerResumeRegistration.add(volunteerRegistrationButton)

