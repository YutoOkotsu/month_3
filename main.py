import asyncio
import logging
from aiogram import types
from bot import bot, dp
from db.chel import chel_router
from House.house import parser_router
from handlers import (
                      start_router,
                      scheduler_router,
                      echo_router,
                      good_router)
from db.ani import init_db, create_tables, populate_db


async def on_startup():
    print('Бот вышел в онлайн')
    init_db()
    create_tables()
    populate_db()


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="Opros", description="Опрос"),
        types.BotCommand(command="catalog", description="Каталог")
    ])

    dp.include_router(start_router)
    dp.include_router(good_router)
    dp.include_router(chel_router)
    dp.include_router(scheduler_router)
    dp.include_router(parser_router)
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
