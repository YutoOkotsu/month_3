from aiogram import types, Router
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message : types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='shop', callback_data="shop"),
             types.InlineKeyboardButton(text='all', callback_data="all")]
        ]
    )
    await message.answer(f"привет {message.from_user.username}", reply_markup=kb)
