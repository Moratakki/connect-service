from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot, storage=storage)
running = [False]
userStatus = [False]
