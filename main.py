import asyncio
import logging

from bot_config import dp, bot, database
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.review_dialog import review_router


async def on_startup():
    database.create_tables()


async def main():
    # Регистрация всех обработчиков
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(review_router)

    # в самом конце
    dp.startup.register(on_startup)

   #запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())