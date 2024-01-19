import asyncio
from aiogram import types
import logging
from bot import bot, dp
from handlers import (pic_router,
                      site_router,
                      start_router,
                      echo_router,
                      myinfo_router,
                      good_router)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="myinfo", description="моя информация"),
        types.BotCommand(command="anime", description="Аниме")

    ])
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(site_router)
    dp.include_router(good_router)
    dp.include_router(echo_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())