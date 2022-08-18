from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

volunteerAcceptButton = KeyboardButton('Принять')
volunteerDeclineButton = KeyboardButton('Отклонить')

volunteerVerificationButtons = ReplyKeyboardMarkup(resize_keyboard=True)
volunteerVerificationButtons.row(volunteerAcceptButton, volunteerDeclineButton)