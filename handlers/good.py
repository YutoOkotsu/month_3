from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


good_router = Router()
# FSM - Finite State Machine
# Конечный автомат
class Good(StatesGroup):
    name = State()
    age = State()
    janr = State()
    phone = State()

def janr_kb():
    # DRY Don't Repeat Yourself
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Аниме"),
                types.KeyboardButton(text="Книги")
            ],
            [
                types.KeyboardButton(text="Фильмы"),
                types.KeyboardButton(text="Сериалы")
            ],
            [
                types.KeyboardButton(text="Косметика"),
                types.KeyboardButton(text="Манги")
            ]
        ]
    )
    return kb

@good_router.message(Command("Opros"))
async def start_registration(message: types.Message, state: FSMContext):
    await state.set_state(Good.name)
    await message.answer("Предлагаем Вам пройти опрос!Можете остановить опрос командой /cancel")
    await message.answer("Как Вас зовут?")


@good_router.message(Command("cancel"))
@good_router.message(F.text.lower() == "отмена")
async def cancel_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Регистрация отменена")


@good_router.message(good_router.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Good.age)
    await message.answer("Сколько Вам лет?")


@good_router.message(Good.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(message.text) < 14 or int(message.text) > 80:
        await message.answer("Возраст должен быть от 14 до 80 лет")
    else:
        age = int(message.text)
        await state.update_data(age=age)
        await state.set_state(Good.janr_kb)
        await message.answer("Какое направление Вы хотите изучать?", reply_markup=janr_kb())


@good_router.message(Good.janr_kb)
async def process_janr(message: types.Message, state: FSMContext):
    await state.update_data(janr=message.text)
    hide_kb = types.ReplyKeyboardRemove()
    await state.set_state(Good.phone)
    await message.answer("Ваш номер телефона?", reply_markup=hide_kb)


