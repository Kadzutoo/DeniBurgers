from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()

# Главное меню
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Меню", callback_data="show_menu")
    builder.button(text="Поддержка", callback_data="help")  # Кнопка поддержки
    return builder.as_markup()

@start_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать в DeniBurgers! \nВыберите действие:",
        reply_markup=main_menu()
    )
