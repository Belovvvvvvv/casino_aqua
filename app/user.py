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
from aiogram.types import Message, CallbackQuery
import config as cfg
from app.database.requests import add_user, get_user
import app.keyboard as keyboard
from app.states import UserStates
from aiogram.fsm.context import FSMContext
from ru.h1guro.cryptopay import create_pay, get_pay
from app.games import dice_games, football_games, basketball_games, boul_games, darts_games
from app.database.requests import add_bet_sum, add_win, add_loss

router = Router()



@router.message(F.text == '/start')
async def main(message: Message):
    await add_user(message.from_user.id)
    await message.answer(cfg.hello_msg.format(first_name=message.from_user.first_name, username=message.from_user.username, name=message.from_user.full_name), reply_markup=keyboard.main_keyboard)

@router.callback_query(F.data == 'start')
async def start(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(cfg.hello_msg.format(first_name=callback.from_user.first_name, username=callback.from_user.username, name=callback.from_user.full_name), reply_markup=keyboard.main_keyboard)
    await state.clear()

@router.callback_query(F.data == 'make_bet')
async def make_bet(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Выберите игру", reply_markup=await keyboard.games_list())
    await state.clear()

@router.callback_query(F.data.startswith('game:'))
async def game_callback(callback: CallbackQuery, state: FSMContext):
    game_type, game_id = callback.data.split(':')[1:]
    await callback.message.edit_text(f"<b>🚀 Введите сумму ставки:</b>", parse_mode="HTML", reply_markup=keyboard.back_keyboard)
    await state.update_data(game_type=game_type)
    await state.update_data(game_id=game_id)
    await state.set_state(UserStates.bet_amount)

@router.message(UserStates.bet_amount)
async def bet_amount(message: Message, state: FSMContext):
    if cfg.min_bet > float(message.text):
        await message.answer(f"<b>❌ Минимальная ставка: {cfg.min_bet}$</b>", parse_mode='HTML')
        return
    if cfg.max_bet < float(message.text):
        await message.answer(f"<b>❌ Максимальная ставка: {cfg.max_bet}$</b>", parse_mode='HTML')
        return
    data = await state.get_data()
    game_type = data.get('game_type')
    game_id = data.get('game_id')
    try:
        bet_amount = float(message.text)
    except ValueError:
        await message.answer("<b>❌ Введите число. Например: 10.05.</b>", parse_mode='HTML')
        return
    await state.update_data(bet_amount=bet_amount)
    try:
        invoice = await create_pay(bet_amount)
        url = invoice.bot_invoice_url
        invoice_id = invoice.invoice_id
        await message.answer(f"<b>Счет на {bet_amount:.2f}$:</b>", parse_mode='HTML', reply_markup=await keyboard.pay_keyboard(url, invoice_id))
        await state.update_data(invoice_id=invoice_id)
    except Exception as e:
        await message.answer(f"<b>❌ Произошла ошибка при создании счета</b>. Отпишите в тех.поддержку: {cfg.support_link}", parse_mode='HTML')

@router.callback_query(F.data.startswith('check_pay:'))
async def check_payment(callback: CallbackQuery, state: FSMContext):
    invoice_id = callback.data.split(':')[1]
    data = await state.get_data()
    bet_amount = data.get('bet_amount')
    game_type = data.get('game_type')
    game_id = data.get('game_id')
    invoice = await get_pay(invoice_id)
    #await add_bet_sum(callback.from_user.id, bet_amount)

    if invoice[0].status == 'paid':
        await callback.message.edit_text("✅ Оплата найдена!\n⌛ Ставка будет отыграна в течение 10 секунд в нашем канале", reply_markup=keyboard.channel_keyboard)
        if game_type == 'dice':
            await dice_games(bet_amount, game_type, game_id, callback.from_user.id)
        if game_type == 'football':
            await football_games(bet_amount, game_type, game_id, callback.from_user.id)
        if game_type == 'darts':
            await darts_games(bet_amount, game_type, game_id, callback.from_user.id)
        if game_type == 'boul':
            await boul_games(bet_amount, game_type, game_id, callback.from_user.id)
        if game_type == 'basketball':
            await basketball_games(bet_amount, game_type, game_id, callback.from_user.id)
    else:
        await callback.answer('❌ Оплата не найдена!')
    await state.clear()

@router.callback_query(F.data == 'profile')
async def profile(callback: CallbackQuery, state: FSMContext):
    user = await get_user(callback.from_user.id)
    bet_sum = user.bet_sum  
    wins = user.wins
    losses = user.losses
    await callback.message.edit_text(f"👤 Ваш профиль:\n\n🆔 UserID: {callback.from_user.id}\n💰 Сумма ставок: {bet_sum:.2f}$\n💰 Выиграно: {wins}\n💸 Проиграно: {losses}", parse_mode='HTML', reply_markup=keyboard.profile_keyboard)
    await state.clear()