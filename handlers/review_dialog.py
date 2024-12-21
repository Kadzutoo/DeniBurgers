import sqlite3

from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot_config import database


review_router = Router()

# FSM-состояния
class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_router.callback_query(F.data == "review")
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Как вас зовут? (Имя должно быть от 2 до 20 символов)")
    await state.set_state(RestourantReview.name)

@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    if len(name) < 2 or len(name) > 50:
        await message.answer("Имя должно быть от 2 до 2 символов. Попробуйте снова.")
        return
    await state.update_data(name=name)
    await message.answer("Укажите ваш номер телефона или Instagram:")
    await state.set_state(RestourantReview.phone_number)

@review_router.message(RestourantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    contact = message.text.strip()
    if len(contact) < 5 or len(contact) > 100:
        await message.answer("Контактная информация должна быть от 5 до 30 символов. Попробуйте снова.")
        return
    await state.update_data(phone_number=contact)

    kb = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=str(i)) for i in range(1, 6)]],
        resize_keyboard=True
    )
    await message.answer("Как вы оцениваете качество еды? (1 - плохо, 5 - отлично)", reply_markup=kb)
    await state.set_state(RestourantReview.food_rating)

@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    if message.text not in {"1", "2", "3", "4", "5"}:
        await message.answer("Введите число от 1 до 5.")
        return
    await state.update_data(food_rating=message.text)

    kb = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=str(i)) for i in range(1, 6)]],
        resize_keyboard=True
    )
    await message.answer("Как вы оцениваете чистоту заведения? (1 - плохо, 5 - отлично)", reply_markup=kb)
    await state.set_state(RestourantReview.cleanliness_rating)

@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    if message.text not in {"1", "2", "3", "4", "5"}:
        await message.answer("Введите число от 1 до 5.")
        return
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("Напишите дополнительные комментарии или жалобы (если есть):")
    await state.set_state(RestourantReview.extra_comments)

@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    comments = message.text
    await state.update_data(extra_comments=comments)
    data = await state.get_data()

 # Сохранение данных в базу
    await database.save_review(data)


@review_router.message(RestourantReview.extra_comments)
async def get_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    await message.answer(
        f"Спасибо за ваш отзыв!\n\n"
        f"Имя: {data['name']}\n"
        f"Контакты: {data['phone_number']}\n"
        f"Оценка еды: {data['food_rating']}\n"
        f"Оценка чистоты: {data['cleanliness_rating']}\n"
        f"Дополнительные комментарии: {data['extra_comments']}"
    )


# конец
    await state.clear()

