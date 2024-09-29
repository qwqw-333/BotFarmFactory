from time import sleep
from random import random, shuffle, randint

from initiator import Initiator
from accounts import TELEGRAM_ACCOUNTS
from bots.base.base import logging
from bots.base.utils import check_proxy
from config import MULTITHREAD, SLEEP_BETWEEN_START
from utils import BOTS
if MULTITHREAD:
    from threading import Thread


def make_account_farmers(account):
    phone = account['phone']
    if proxy := account.get('proxy'):
        proxies = dict(http=proxy, https=proxy)
        proxy = proxy if check_proxy(proxies=proxies) else None
    try:
        initiator = Initiator(phone)
    except Exception as e:
        logging.error(f'{phone} Error: {e}')
        return []
    farmers = []
    for farmer_class in BOTS:
        try:
            farmer = farmer_class(initiator=initiator, proxy=proxy)
        except Exception as e:
            logging.error(f'{farmer_class.name} init error: {e}')
            continue
        if not farmer.is_alive:
            continue
        farmers.append(farmer)
    initiator.disconnect()
    sleep(random() * 10)
    return farmers

def main(farmers):
    while True:
        shuffle(farmers)
        for farmer in farmers:
            farmer.proceed_farming()
            sleep(1 + random())
        sleep(1)

def farm_in_thread(phone, delay):
    import asyncio
    if delay > 0:
        logging.info(f"{phone['phone']} | Wait {delay} seconds before start")
        sleep(delay)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    main(make_account_farmers(phone))


if MULTITHREAD:
    for account in TELEGRAM_ACCOUNTS:
        delay = randint(*SLEEP_BETWEEN_START) if len(TELEGRAM_ACCOUNTS) > 1 else 0
        Thread(target=farm_in_thread, args=(account, delay,)).start()
    while True:
        input()
else:
    farmers = []
    for account in TELEGRAM_ACCOUNTS:
        farmers += make_account_farmers(account)
    print('')
    farmer_names = ", ".join(set([farmer.name.lower() for farmer in farmers]))
    logging.info("Найдены фармеры: {farmer_names}".format(farmer_names=farmer_names))

    if not farmers:
        exit()

    main(farmers)
