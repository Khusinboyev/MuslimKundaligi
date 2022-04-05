from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

TOKEN = '5125502809:AAGW0dbip1_VMQxb3EAJ5d45rKIcnvEARfQ'

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=storage)