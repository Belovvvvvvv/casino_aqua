from aiocryptopay import AioCryptoPay, Networks
import config as cfg

cp = AioCryptoPay(token=cfg.CRYPTO_PAY_TOKEN, network=Networks.MAIN_NET)

async def create_pay(amount):
    invoice = await cp.create_invoice(amount=amount, fiat='USD', currency_type='fiat')
    return invoice

async def get_pay(invoice_id):
    invoice = await cp.get_invoices(invoice_ids=invoice_id)
    return invoice


async def create_check(amount):
    try:
        check = await cp.create_check(asset='USDT', amount=amount)
        return check.bot_check_url
    except Exception as e:
        print(f"Ошибка при создании чека: {e}")
        return False

async def get_balance():
    balance = await cp.get_balance()
    return balance

