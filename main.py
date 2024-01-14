import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.start import start_router
from handlers.pic import pic_router
from handlers.myinfo import myinfo_router
from handlers.echo import echo_router


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="myinfo", description="моя информация"),
        types.BotCommand(command="course", description="Курсы")

    ])
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(echo_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())