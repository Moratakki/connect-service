from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

applicantButton = KeyboardButton("/Абитуриент")
volunteerButton = KeyboardButton("/Волонтёр")

statusDefiningButtons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)

statusDefiningButtons.row(applicantButton, volunteerButton)
