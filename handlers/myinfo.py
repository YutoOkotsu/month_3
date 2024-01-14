from aiogram import Router, types
from aiogram.filters import Command
from pprint import pprint

myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def myinfo(message: types.Message):
    pprint(message)
    await message.answer(f"Ваш ник: {message.from_user.full_name}Ваше id: {message.from_user.id}, Ваше имя: {message.from_user.first_name}")

