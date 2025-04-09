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

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from app.database.models import User, async_session, Stats
from sqlalchemy.exc import IntegrityError

async def add_user(user_id: int):
    async with async_session() as session:
        async with session.begin():  
            user = await session.scalar(select(User).where(User.id == user_id))
            if not user:
                user = User(id=user_id)  
                session.add(user)           
            await session.commit()

async def get_user(user_id: int):
    async with async_session() as session:
        async with session.begin():
            user = await session.scalar(select(User).where(User.id == user_id))
            return user

async def get_or_create_user(session, user_id):
    user = await session.scalar(select(User).where(User.id == user_id))
    if not user:
        user = User(id=user_id)
        session.add(user)
    return user

async def get_or_create_stats(session):
    stats = await session.scalar(select(Stats).where(Stats.id == 1))
    if not stats:
        stats = Stats(id=1)
        session.add(stats)
    return stats

async def add_bet_sum(user_id, bet_sum):
    async with async_session() as session:
        async with session.begin():
            try:
                user = await get_or_create_user(session, user_id)
                user.bet_sum += bet_sum

                stats = await get_or_create_stats(session)
                stats.total_bets += bet_sum

                await session.flush()
                await session.commit()
            except IntegrityError as e:
                await session.rollback()
                raise ValueError(f"Ошибка при добавлении суммы ставки: {e}")

async def add_win(user_id: int):
    async with async_session() as session:
        async with session.begin():
            try:
                user = await get_or_create_user(session, user_id)
                user.wins += 1

                stats = await get_or_create_stats(session)
                stats.total_wins += 1

                await session.flush()
                await session.commit()
            except IntegrityError as e:
                await session.rollback()
                raise ValueError(f"Ошибка при добавлении победы: {e}")

async def add_loss(user_id: int):
    async with async_session() as session:
        async with session.begin():
            try:
                user = await get_or_create_user(session, user_id)
                user.losses += 1

                stats = await get_or_create_stats(session)
                stats.total_losses += 1

                await session.flush()
                await session.commit()
            except IntegrityError as e:
                await session.rollback()
                raise ValueError(f"Ошибка при добавлении поражения: {e}")

async def get_stats():
    async with async_session() as session:
        async with session.begin():
            stats = await session.scalar(select(Stats).where(Stats.id == 1))
            return stats
