import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.support import support_router

token = dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()

# Регистрация роутеров
dp.include_router(start_router)
dp.include_router(menu_router)
dp.include_router(support_router)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
