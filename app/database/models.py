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

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped, DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, Boolean, BigInteger
import asyncio

DATABASE_URL = "sqlite+aiosqlite:///db.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    bet_sum: Mapped[float] = mapped_column(Float, default=0)
    wins: Mapped[int] = mapped_column(Integer, default=0)
    losses: Mapped[int] = mapped_column(Integer, default=0)

class Stats(Base):
    __tablename__ = "stats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    total_wins: Mapped[int] = mapped_column(Integer, default=0)
    total_losses: Mapped[int] = mapped_column(Integer, default=0)
    total_bets: Mapped[float] = mapped_column(Float, default=0)

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("База данных успешно инициализирована")
    except Exception as e:
        print(f"Ошибка инициализации базы данных: {e}")


if __name__ == "__main__":
    asyncio.run(init_db())