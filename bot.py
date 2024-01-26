from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)




