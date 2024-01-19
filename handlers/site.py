from aiogram import Router, types, F
from aiogram.filters import Command
from pprint import pprint

from bot import bot

site_router = Router()

@site_router.callback_query(F.data=="site")
async def site(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="фильм", callback_data="film"),
             types.InlineKeyboardButton(text="сериал", callback_data="serial"),
             types.InlineKeyboardButton(text="аниме", callback_data="anime")]
        ]
    )
    await bot.send_message(chat_id=call.message.chat.id,
    text="вот все категории",
    reply_markup=kb)

@site_router.callback_query(F.data=="film")
async def film(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id,
                           text="вы нажали фильмы")

@site_router.callback_query(F.data == "serial")
async def serial(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id,
                           text="вы нажали сериал")

@site_router.callback_query(F.data=="anime")
async def anime(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id,
                           text="вы нажали аниме")