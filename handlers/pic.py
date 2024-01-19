from aiogram import Router, types
from aiogram.filters import Command
import os
import random

pic_router = Router()



@pic_router.message(Command("pic"))
async def send_pic(message: types.Message):
    photo_folder = "image"
    photos = os.listdir(photo_folder)
    photo_name = random.choice(photos)
    photo = types.FSInputFile(os.path.join(photo_folder, photo_name))
    await message.answer_photo(photo=photo, caption="Вот ваша случайная аниме девушка!")