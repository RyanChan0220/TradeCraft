__author__ = 'ryan'

from TradeSys.TradeFunc import *

START_MONEY = 10000


def craft_init():
    trade_set_start_money(START_MONEY)
    print trade_get_start_money()
    print trade_get_rest_money()


def craft_cycle():
    print trade_order_shares("sh600000", 100)
    print trade_get_start_money()
    print trade_get_rest_money()
