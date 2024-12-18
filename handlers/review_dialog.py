from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

review_router = Router()

# FSM-состояния
class RestorantReview(StatesGroup):
    name = State()
    phone_or_instagram = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

# Начало FSM
@review_router.callback_query(F.data == "review")
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestorantReview.name)

# Получение имени
@review_router.message(RestorantReview.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона или Instagram?")
    await state.set_state(RestorantReview.phone_or_instagram)

# Получение телефона или Instagram
@review_router.message(RestorantReview.phone_or_instagram)
async def get_contact(message: types.Message, state: FSMContext):
    await state.update_data(phone_or_instagram=message.text)
    await message.answer("Как вы оцениваете качество еды? (от 1 до 5)")
    await state.set_state(RestorantReview.food_rating)

# Оценка еды
@review_router.message(RestorantReview.food_rating)
async def get_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await message.answer("Как оцениваете чистоту заведения? (от 1 до 5)")
    await state.set_state(RestorantReview.cleanliness_rating)

# Оценка чистоты
@review_router.message(RestorantReview.cleanliness_rating)
async def get_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("Есть ли у вас дополнительные комментарии?")
    await state.set_state(RestorantReview.extra_comments)

# Дополнительные комментарии
@review_router.message(RestorantReview.extra_comments)
async def get_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    review_data = await state.get_data()
    await message.answer(
        f"Спасибо за ваш отзыв!\n\n"
        f"Имя: {review_data['name']}\n"
        f"Контакты: {review_data['phone_or_instagram']}\n"
        f"Оценка еды: {review_data['food_rating']}\n"
        f"Оценка чистоты: {review_data['cleanliness_rating']}\n"
        f"Дополнительные комментарии: {review_data['extra_comments']}"
    )
    await state.clear()



