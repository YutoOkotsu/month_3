import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from handlers import (start_router, pic_router)


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

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
    dp.include_router(start_router)
    dp.include_router(pic_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())