__author__ = 'ryan'

import collections
from BackTestSys.BackTest import back_get_timer_now
from TradeSys.TradeSQL import *

OrderStatus = {"Cancel": 0, "Dealed": 1, "Submited": 2}
orders = collections.OrderedDict()
orders_count = 0


def tradelogic_get_order_status(order_id):
    if order_id in orders:
        return orders[order_id]
    else:
        return None


def tradelogic_get_order_id():
    global orders_count
    ret = orders_count
    orders[orders_count] = ()
    orders_count += 1
    return ret


#TODO 交易精度为1分钟
def tradelogic_get_price(stock_id):
    now = back_get_timer_now()
    price = tradesql_get_now_price_by_date(stock_id, now)
    return price


def tradelogic_is_bargaining(stock_id):
    pass
    return True


def tradelogic_transaction_submit(order_id, stock_id, amount, price):
    #check stock status
    if tradelogic_is_bargaining(stock_id) is False:
        return OrderStatus["Cancel"]
    #check amount
    if amount >= 0:
        pass
    else:
        pass
    return OrderStatus["Dealed"]