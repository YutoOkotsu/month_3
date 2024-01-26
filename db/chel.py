from aiogram import types, Router, F
from db.ani import get_products_by_cat, get_products

chel_router = Router()
@chel_router.callback_query(F.data == 'shop')
async def products(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='book', callback_data="book"),
             types.InlineKeyboardButton(text='comics', callback_data="comics"),
             types.InlineKeyboardButton(text='manga', callback_data="manga")]
        ]
    )
    await call.message.answer('что вы хотите посмотреть', reply_markup=kb)


@chel_router.callback_query(F.data == 'book')
async def book(call: types.CallbackQuery):
    pro = get_products_by_cat(1)
    for product in pro:
        await call.message.answer(f'название {product[1]}\n'
                                  f'цена {product[2]}')

@chel_router.callback_query(F.data == 'comics')
async def comics(call: types.CallbackQuery):
    pro = get_products_by_anime(2)
    for product in pro:
        await call.message.answer(f'название {product[1]}\n'
                                  f'цена {product[2]}')

@chel_router.callback_query(F.data == 'manga')
async def manga(call: types.CallbackQuery):
    pro = get_products_by_cat(3)
    for product in pro:
        await call.message.answer(f'название {product[1]}\n'
                                  f'цена {product[2]}')

@chel_router.callback_query(F.data == 'all')
async def product(call: types.CallbackQuery):
    pro = get_products()
    for product in pro:
        await call.message.answer(f'название {product[1]}\n'
                                  f'цена {product[2]}')