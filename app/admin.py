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

from aiogram import Router, F
from aiogram.types import Message
import config as cfg
from aiogram.filters import Filter
from ru.h1guro.cryptopay import get_balance
from app.database.requests import get_stats
admin = Router()

class AdminProtect(Filter):
    def __init__(self):
        self.admins = cfg.ADMIN_LIST

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins

@admin.message(F.text == '/adm', AdminProtect())
async def start(message: Message):
    balance = await get_balance()

    positive_balances = [bal for bal in balance if bal.available > 0]

    if not positive_balances:
        await message.answer('💸 Баланс криптобота: 0')
        return

    balance_message = '💸 Баланс криптобота:\n'
    for bal in positive_balances:
        balance_message += f'{bal.currency_code}: {bal.available}\n'

    await message.answer(balance_message)
    stats = await get_stats()
    await message.answer(f'💰 Выиграно: {stats.total_wins}\n💸 Проиграно: {stats.total_losses}\n💰 Всего ставок: {stats.total_bets}$')

