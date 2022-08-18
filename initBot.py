from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import sqlite3



userDB = sqlite3.connect('users.db')
crsr = userDB.cursor()
userDB.execute("CREATE TABLE IF NOT EXISTS {}(TelegramID, Username, FullName, City, University, Faculty, Confirmed)".format('volunteers'))
userDB.commit()
userDB.execute("CREATE TABLE IF NOT EXISTS {}(TelegramID, Username, FullName, Education )".format('applicants'))
userDB.commit()

storage = MemoryStorage()

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot, storage=storage)
stopReceivingRequest = [False]
