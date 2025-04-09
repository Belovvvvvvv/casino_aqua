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

import config as cfg
from aiogram import Bot
from aiogram.types import Message
import asyncio
from ru.h1guro.cryptopay import create_check
import app.keyboard as keyboard
from app.database.requests import add_win, add_loss

bot = Bot(token=cfg.BOT_TOKEN)

async def dice_games(bet_amount, game_type, game_id, player_id):
    await asyncio.sleep(3)
    try:
        print(game_type, game_id)
        user = await bot.get_chat(player_id)
        first_name = user.first_name
        username = user.username
        msg = await bot.send_message(cfg.channel_id, cfg.bet_msg.format(bet_amount=bet_amount, game_type=game_type, game_id=game_id, first_name=first_name, username=username), parse_mode='HTML')
        msgid = msg.message_id
        message: Message = await bot.send_dice(chat_id=cfg.channel_id, emoji='🎲', reply_to_message_id=msgid)
        
        dice_value = message.dice.value
        await asyncio.sleep(3)
        print(dice_value)

        game = next((g for g in cfg.games if g['callback_data'] == game_id), None)
        if not game:
            print(f"Игра с game_id {game_id} не найдена")
            return

        coefficent = game['coefficent']

        if game_id == 'even':
            if dice_value % 2 == 0:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)
        elif game_id == 'odd':
            if dice_value % 2 != 0:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)
    except Exception as e:
        print(f"Ошибка при выполнении игры: {e}")

async def football_games(bet_amount, game_type, game_id, player_id):
    await asyncio.sleep(3)
    try:
        user = await bot.get_chat(player_id)
        first_name = user.first_name
        username = user.username
        msg = await bot.send_message(cfg.channel_id, cfg.bet_msg.format(bet_amount=bet_amount, game_type=game_type, game_id=game_id, first_name=first_name, username=username), parse_mode='HTML')
        msgid = msg.message_id
        message: Message = await bot.send_dice(cfg.channel_id, emoji='⚽', reply_to_message_id=msgid)
        dice_value = message.dice.value
        await asyncio.sleep(3)
        print(dice_value)

        game = next((g for g in cfg.games if g['callback_data'] == game_id), None)
        if not game:
            print(f"Игра с game_id {game_id} не найдена")
            return

        coefficent = game['coefficent']
        if game_id == 'goal':
            if dice_value >= 3:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)
        if game_id == 'miss':
            if dice_value <= 2:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)

    except Exception as e:
        print(f"Ошибка при выполнении игры: {e}")


async def basketball_games(bet_amount, game_type, game_id, player_id):
    await asyncio.sleep(3)
    try:
        user = await bot.get_chat(player_id)
        first_name = user.first_name
        username = user.username
        msg = await bot.send_message(cfg.channel_id, cfg.bet_msg.format(bet_amount=bet_amount, game_type=game_type, game_id=game_id, first_name=first_name, username=username), parse_mode='HTML')
        msgid = msg.message_id
        message: Message = await bot.send_dice(cfg.channel_id, emoji='🏀', reply_to_message_id=msgid)
        dice_value = message.dice.value
        await asyncio.sleep(3)
        print(dice_value)

        game = next((g for g in cfg.games if g['callback_data'] == game_id), None)
        if not game:
            print(f"Игра с game_id {game_id} не найдена")
            return

        coefficent = game['coefficent']
        if game_id == 'goal':
            if dice_value > 3:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)
        if game_id == 'miss':
            if dice_value <= 3:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)

    except Exception as e:
        print(f"Ошибка при выполнении игры: {e}")

async def boul_games(bet_amount, game_type, game_id, player_id):
    await asyncio.sleep(3)
    try:
        user = await bot.get_chat(player_id)
        first_name = user.first_name
        username = user.username
        msg = await bot.send_message(cfg.channel_id, cfg.bet_msg.format(bet_amount=bet_amount, game_type=game_type, game_id=game_id, first_name=first_name, username=username), parse_mode='HTML')
        msgid = msg.message_id

        while True:
            message: Message = await bot.send_dice(cfg.channel_id, emoji='🎳', reply_to_message_id=msgid)
            message2: Message = await bot.send_dice(cfg.channel_id, emoji='🎳', reply_to_message_id=msgid)
            dice_value1 = message.dice.value
            dice_value2 = message2.dice.value
            await asyncio.sleep(3)
            print(dice_value1, dice_value2)

            if dice_value1 != dice_value2:
                break

        game = next((g for g in cfg.games if g['callback_data'] == game_id), None)
        if not game:
            print(f"Игра с game_id {game_id} не найдена")
            return

        coefficent = game['coefficent']
        if game_id == 'duel':
            if dice_value1 > dice_value2:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)

    except Exception as e:
        print(f"Ошибка при выполнении игры: {e}")

async def darts_games(bet_amount, game_type, game_id, player_id):
    await asyncio.sleep(3)
    try:
        user = await bot.get_chat(player_id)
        first_name = user.first_name
        username = user.username
        msg = await bot.send_message(cfg.channel_id, cfg.bet_msg.format(bet_amount=bet_amount, game_type=game_type, game_id=game_id, first_name=first_name, username=username), parse_mode='HTML')
        msgid = msg.message_id

        while True:
            message: Message = await bot.send_dice(cfg.channel_id, emoji='🎯', reply_to_message_id=msgid)
            message2: Message = await bot.send_dice(cfg.channel_id, emoji='🎯', reply_to_message_id=msgid)
            dice_value1 = message.dice.value
            dice_value2 = message2.dice.value
            await asyncio.sleep(3)
            print(dice_value1, dice_value2)

            if dice_value1 != dice_value2:
                break  

        game = next((g for g in cfg.games if g['callback_data'] == game_id), None)
        if not game:
            print(f"Игра с game_id {game_id} не найдена")
            return

        coefficent = game['coefficent']
        if game_id == 'duel':
            if dice_value1 > dice_value2:
                await add_win(player_id)
                await bot.send_message(cfg.channel_id, cfg.win_msg.format(win_amount=bet_amount * coefficent, username=username, first_name=first_name), reply_to_message_id=msgid)
                try:
                    check = await create_check(bet_amount * coefficent)
                    if check == False:
                        await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                        for admin in cfg.ADMIN_LIST:
                            await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
                    if check:
                        await bot.send_message(player_id, cfg.pm_win_msg, reply_markup=await keyboard.get_check(check))
                except Exception as e:
                    print(f"Ошибка при создании чека: {e}")
                    await bot.send_message(player_id, cfg.pm_error_win_msg.format(support_link=cfg.support_link))
                    for admin in cfg.ADMIN_LIST:
                        await bot.send_message(admin, f"❌ Ошибка при создании чека! {player_id} {bet_amount * coefficent}")
            else:
                await add_loss(player_id)
                await bot.send_message(player_id, cfg.pm_lose_msg)
                await bot.send_message(cfg.channel_id, cfg.lose_msg, reply_to_message_id=msgid)

    except Exception as e:
        print(f"Ошибка при выполнении игры: {e}")   