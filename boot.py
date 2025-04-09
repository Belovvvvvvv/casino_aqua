#  _      _        _                    _ 
# | |__  / |  ___ | |  ___   _   _   __| |
# | '_ \ | | / __|| | / _ \ | | | | / _` |
# | | | || || (__ | || (_) || |_| || (_| |
# |_| |_||_| \___||_| \___/  \__,_| \__,_|

# ПРОСПОНСИРОВАНО ЛУЧШИМ ХОСТИНГОМ ДЛЯ СКРИПТОВ НА PYTHON/NODEJS.
# - Сервера от 30руб*
# - Быстрая скорость ботов
# - Стабильность 
# t.me/h1cloudbot


# *актуально на момент 12.03.2025

from aiogram import Bot, Dispatcher
import asyncio 
from app.user import router as user_router
from app.admin import admin as admin_router
from config import BOT_TOKEN
import logging
import os
from datetime import datetime
from app.database.models import init_db

os.makedirs('logs', exist_ok=True)

log_file = f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(admin_router)
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.info("Запуск бота...")
    asyncio.run(main())

