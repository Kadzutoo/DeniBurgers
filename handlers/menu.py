from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_router = Router()

# Главное меню
def food_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Пицца", callback_data="pizza")
    builder.button(text="Салаты", callback_data="salads")
    builder.button(text="Напитки", callback_data="drinks")
    builder.button(text="Назад", callback_data="back_to_main")
    return builder.as_markup()

# Обработка открытия меню
@menu_router.callback_query(F.data == "show_menu")
async def show_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите категорию из меню:",
        reply_markup=food_menu()
    )

# Обработка категорий еды
@menu_router.callback_query()
async def handle_category(callback: CallbackQuery):
    if callback.data == "pizza":
        await callback.message.edit_text(
            "Доступные пиццы:\n1. Маргарита\n2. Пепперони\n3. Гавайская",
            reply_markup=food_menu()
        )
    elif callback.data == "salads":
        await callback.message.edit_text(
            "Доступные салаты:\n1. Цезарь\n2. Греческий\n3. Оливье",
            reply_markup=food_menu()
        )
    elif callback.data == "drinks":
        await callback.message.edit_text(
            "Доступные напитки:\n1. Кола\n2. Спрайт\n3. Минеральная вода",
            reply_markup=food_menu()
        )
    elif callback.data == "back_to_main":
        # Вернуться в главное меню
        await callback.message.edit_text(
            "Вы вернулись в главное меню. Выберите действие:",
            reply_markup=main_menu()
        )

# Главное меню (используется при возврате назад)
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text=" Меню", callback_data="show_menu")
    builder.button(text=" Помощь", callback_data="help")
    builder.adjust(1)
    return builder.as_markup()
