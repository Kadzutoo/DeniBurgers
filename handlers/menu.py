from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_router = Router()

# Клавиатура для меню еды
def food_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Пицца", callback_data="pizza")
    builder.button(text=" Салаты", callback_data="salads")
    builder.button(text=" Напитки", callback_data="drinks")
    builder.button(text=" Назад", callback_data="back_to_main")
    builder.adjust(1)
    return builder.as_markup()

# Обработчик кнопки " Пицца"
@menu_router.callback_query(F.data == "pizza")
async def show_pizza(callback: CallbackQuery):
    await callback.message.edit_text(
        " Доступные пиццы:\n1. Маргарита\n2. Пепперони\n3. Гавайская",
        reply_markup=food_menu()
    )

# Обработчик кнопки "Салаты"
@menu_router.callback_query(F.data == "salads")
async def show_salads(callback: CallbackQuery):
    await callback.message.edit_text(
        " Доступные салаты:\n1. Цезарь\n2. Греческий\n3. Оливье",
        reply_markup=food_menu()
    )

# Обработчик кнопки " Напитки"
@menu_router.callback_query(F.data == "drinks")
async def show_drinks(callback: CallbackQuery):
    await callback.message.edit_text(
        " Доступные напитки:\n1. Кола\n2. Спрайт\n3. Минеральная вода",
        reply_markup=food_menu()
    )

# Обработчик кнопки "Назад" (возврат в главное меню)
@menu_router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    from handlers.start import main_menu  # Импортируем главное меню
    await callback.message.edit_text(
        "Вы вернулись в главное меню. Выберите действие:",
        reply_markup=main_menu()
    )
