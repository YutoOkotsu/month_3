from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from db.ani import save_good_data
from клавиатура.kb import janr_kb

good_router = Router()
# FSM - Finite State Machine
# Конечный автомат
class Good(StatesGroup):
    name = State()
    age = State()
    janr = State()
    favorite_anime = State()


@good_router.message(Command("Опрос"))
async def start_registration(message: types.Message, state: FSMContext):
    await state.set_state(Good.name)
    await message.answer("Предлагаем Вам пройти опрос!Можете остановить опрос командой /cancel")
    await message.answer("Как Вас зовут?")


@good_router.message(Command("cancel"))
@good_router.message(F.text.lower() == "отмена")
async def cancel_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Регистрация отменена")


@good_router.message(Good.name)
async def process_name(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer("В имени не могут быть цифры!")
    else:
        await state.update_data(name=message.text)
        await state.set_state(Good.age)
        await message.answer("Сколько Вам лет?")


@good_router.message(Good.age)
async def process_age(message: types.Message, state: FSMContext):
    print("ggfgg")
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(message.text) < 12 or int(message.text) > 80:
        await message.answer("Возраст должен быть от 12 до 80 лет")
    else:
        age = int(message.text)
        await state.update_data(age=age)
        await state.set_state(Good.favorite_anime)
        await message.answer("Какое ваше любимое аниме?")


@good_router.message(Good.favorite_anime)
async def process_favorite_anime(message: types.Message, state: FSMContext):
    await state.update_data(favorite_anime=message.text)
    await state.set_state(Good.janr)
    await message.answer("Какой ваш любимый жанр?", reply_markup=janr_kb())


@good_router.message(Good.janr)
async def process_janr(message: types.Message, state: FSMContext):
    await state.update_data(janr=message.text)
    data = await state.get_data()
    await message.answer("Ваш любимый персонаж?")
    await state.clear()
    save_good_data(data)
    await state.clear()
