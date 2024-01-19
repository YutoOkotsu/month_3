from aiogram import Router, types
from aiogram.filters import Command
from pprint import pprint
from aiogram import F

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Сайт", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Инстаграм", url="https://instagram.com/"),
                types.InlineKeyboardButton(text="Телеграм", url="https://t.me/geekskg"),
            ],
            [
                types.InlineKeyboardButton(text="Об о мне и о проекте", callback_data="anime"),
                types.InlineKeyboardButton(text="site", callback_data="site")
            ]
        ]
    )
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}", reply_markup=kb)


@start_router.callback_query(F.data == "anime")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("Здесь мы хотим рассказать о аниме, фильмы и сериалы")