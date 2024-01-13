import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# обработка команды
# handler
@dp.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ")
@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    photo_folder = "image"
    photos = os.listdir(photo_folder)
    photo_name = random.choice(photos)
    photo = types.FSInputFile(os.path.join(photo_folder, photo_name))
    await message.answer_photo(photo=photo, caption="Вот ваша случайная аниме девушка!")
@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    pprint(message)
    await message.answer(f"Ваш ник: {message.from_user.full_name}Ваше id: {message.from_user.id}, Ваше имя: {message.from_user.first_name}")
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="myinfo", description="моя информация"),

    ])
    # запуск бота
    await dp.start_polling(bot)

if name == 'main':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())