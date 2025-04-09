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

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import games
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import config as cfg 

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💰 Сделать ставку", callback_data="make_bet"), InlineKeyboardButton(text="👤 Профиль", callback_data="profile")]
    ]
)

profile_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="start")]
    ]
)

async def get_check(link):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="💰 Забрать выигрыш", url=link))
    builder.add(InlineKeyboardButton(text="🚀 Играть еще", callback_data="make_bet"))
    builder.adjust(1)
    return builder.as_markup()

async def games_list():
    builder = InlineKeyboardBuilder()
    for game in games:
        builder.add(InlineKeyboardButton(text=f'{game["name"]} / {game["coefficent"]}x', callback_data=f"game:{game['type']}:{game['callback_data']}"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="🔙 Назад", callback_data="start"))
    return builder.as_markup()

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="make_bet")]
    ]
)

async def pay_keyboard(invoice_link, invoice_id):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="💳 Оплатить", url=invoice_link))
    builder.add(InlineKeyboardButton(text=f"↪ Проверить оплату", callback_data=f"check_pay:{invoice_id}"))
    builder.add(InlineKeyboardButton(text="🔙 Назад", callback_data="make_bet"))
    builder.adjust(1)
    return builder.as_markup()

channel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти в канал", url=cfg.game_link)]
    ]
)
