from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()

# Главное меню
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Меню", callback_data="show_menu")
    builder.button(text="Оставить отзыв", callback_data="review")
    builder.adjust(1)
    return builder.as_markup()

# Обработчик команды /start
@start_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать в DeniBurger!\nВыберите действие:",
        reply_markup=main_menu()
    )

# Обработчик кнопки "Меню"
@start_router.callback_query(F.data == "show_menu")
async def handle_menu(callback: CallbackQuery):
    from handlers.menu import food_menu
    await callback.message.edit_text(
        "Выберите категорию из меню:",
        reply_markup=food_menu()
    )


# Обработчик кнопки "Оставить отзыв"
@start_router.callback_query(F.data == "start_review")
async def handle_review(callback: CallbackQuery):
    from handlers.review_dialog import RestourantReview
    from aiogram.fsm.context import FSMContext
    await RestourantReview(
        callback,
        FSMContext(bot=callback.bot, chat=callback.message.chat.id, user=callback.from_user.id)
    )

