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

# Основые настройки

BOT_TOKEN = "7090737490:AAEYFkvY4W_XfhS5VXl6WrubkUNQvQRa0cs" # Токен бота из BotFather
CRYPTO_PAY_TOKEN = "367735:AAhHKsvllJmCm5l5Buq6zl7j7T4woXXY6jU" # Токен CryptoBot (@send -> /start -> Crypto Pay -> создать приложение -> безопасность -> createcheck -> включаешь -> transfer -> включаешь -> назад -> Изменить приложение -> меняешь название -> назад -> api токен -> ставишь токен)
ADMIN_LIST = [8137917041] # ID Админов

# Если вы хотите дописать какую-то игру, то нужно добавить ее в список, а так-же app/games.py нужно дописать её обработчик.

# Если вы не знаете программирование, но хотите добавить игру, могу помочь вам за копеечку, мой тг: https://t.me/h1gurodev

# Настройки для бота    
games = [
    {
        "type": "dice",
        "name": "Куб чёт",
        "coefficent": 1.1,
        "callback_data": "even"
    },
    {
        "type": "dice",
        "name": "Куб нечёт",
        "coefficent": 1.1,
        "callback_data": "odd"
    },
    {
        "type": "football",
        "name": "Футбол гол",
        "coefficent": 1.1,
        "callback_data": "goal"
    },
    {
        "type": "football",
        "name": "Футбол мимо",
        "coefficent": 1.1,
        "callback_data": "miss"
    },
    {
        "type": "darts",
        "name": "Дартс дуэль",
        "coefficent": 1.1,
        "callback_data": "duel"
    },
    {
        "type": "boul",
        "name": "Боулинг дуэль",
        "coefficent": 1.1,
        "callback_data": "duel"
    },
    {
        "type": "basketball",
        "name": "Баскетбол попал",
        "coefficent": 1.1,
        "callback_data": "goal"
    },
    {
        "type": "basketball",
        "name": "Баскетбол мимо",
        "coefficent": 1.1,
        "callback_data": "miss"
    },

]
max_bet = 100 # Максимальная ставка
min_bet = 0.1 # Минимальная ставка
channel_id = "123213213" # ID канала отыгрыша ставок
hello_msg = """
Привет, {first_name}
Это казино бот💰""" # Сообщение на /start, {username} - юзернейм, {name} - Имя пользователя
bet_msg = """
<b>✅ Новая ставка!</b>
<b>Сумма ставки:</b> {bet_amount}$
<b>Режим игры:</b> {game_type}
<b>Тип игры:</b> {game_id}
<b>Имя пользователя:</b> {first_name}
""" # bet_amount - сумма ставки, game_type - тип ставки, game_id - id ставки, first_name - имя пользователя, username - юзернейм
win_msg = """
✅ Ставка выиграла!
Сумма выигрыша: {win_amount:.2f}$
""" # win_amount - сумма выигрыша, username - юзернейм, first_name - имя пользователя
lose_msg = """
❌ Ставка проиграла!
"""
pm_win_msg = """
Победа! Заберите свой выигрыш!
"""
pm_lose_msg = """
Проигрыш!
"""
pm_error_win_msg = """Победа!
Выигрыш будет начислен администрацией вручную! Для этого отпишите админу в лс {support_link}""" # support_link - ссылка на ТП

# Ссылки
support_link = "https://t.me/h1gurodev" # Ссылка на ТП
rules_link = "https://t.me/h1cloud/1" # Ссылка на правила
news_link = "https://t.me/h1cloud" # Ссылка на новостной
game_link = "https://t.me/h1cloud" # Ссылка на канал отыгрыша ставок
