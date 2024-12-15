from aiogram import Router
from aiogram import Router, F, types
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command

support_router = Router()

# Обработчик команды /support
@support_router.message(Command("support"))
async def support_command_handler(message: Message):
    await message.answer(
        "Вы обратились в поддержку. Напишите ваш вопрос, и оператор свяжется с вами."
    )

# Обработчик кнопки "Поддержка"
@support_router.callback_query(F.data == "help")
async def help_callback_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Это меню поддержки:\n"
        "1. Если у вас есть вопросы о меню, напишите их здесь.\n"
        "2. Для жалоб используйте команду /complaint.\n\n"
        "Мы свяжемся с вами как можно скорее!"
    )
