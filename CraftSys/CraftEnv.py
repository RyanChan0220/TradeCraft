__author__ = 'ryan'

from TradeSys.TradeFunc import *

START_MONEY = 100000


def craft_init():
    trade_set_start_money(START_MONEY)


def craft_cycle():
    print trade_get_rest_money()
    print trade_order_shares("sh600000", 1000)
    print trade_get_rest_money()
    print trade_order_value("sh600000", -10000)
    print trade_get_rest_money()
    print trade_order_target_value("sh600000", 50000)
    print trade_get_rest_money()
    print trade_order_lots("sh600000", -5)
    print trade_get_rest_money()
    print trade_order_percent("sh600000", 1)
    print trade_get_rest_money()
    print trade_order_target_percent("sh600000", 0.5)
    print trade_get_rest_money()
