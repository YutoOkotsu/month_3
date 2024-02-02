from aiogram import types



def janr_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Романтика"),
                types.KeyboardButton(text="Фентези")
            ],
            [
                types.KeyboardButton(text="Сенён"),
                types.KeyboardButton(text="Драма")
            ],
            [
                types.KeyboardButton(text="Прикючения"),
                types.KeyboardButton(text="Комедия ")
            ],
        ]
    )

    return kb
