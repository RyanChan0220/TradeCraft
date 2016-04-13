__author__ = 'ryan'

import collections
from BackTestSys.BackTest import *
from TradeSys.TradeSQL import *
from TradeFunc import log_trade
import datetime
import math

OrderStatus = {"Empty": 0, "Deal": 1, "Submit": 2, "Cancel": 3}
Orders = collections.OrderedDict()
StartTime = back_get_start_time()


def tradelogic_set_start_time(start_time):
    StartTime = start_time


def tradelogic_cycle():
    #check orders
    # TODO trade accuracy is 1 minute
    tradelogic_cycle.count += 1
    time_now = StartTime + datetime.timedelta(minutes=tradelogic_cycle.count)
    log_trade.info("tradelogic %s" + str(time_now))
tradelogic_cycle.count = 0


def tradelogic_get_order_status(order_id):
    if order_id in Orders:
        return Orders[order_id]
    else:
        return OrderStatus["Empty"]


def tradelogic_set_order_status(order_id, status=OrderStatus["Empty"]):
    if order_id in Orders:
        Orders[order_id] = status
    else:
        pass


def __tradelogic_get_order_id__():
    Orders[__tradelogic_get_order_id__.count] = OrderStatus["Empty"]
    __tradelogic_get_order_id__.count += 1
    return __tradelogic_get_order_id__.count
__tradelogic_get_order_id__.count = 0


def tradelogic_get_price(stock_id):
    now = back_get_timer_now()
    price = tradesql_get_minute_open_price_by_date(stock_id, now)
    return price


def tradelogic_is_bargaining(stock_id):
    now = back_get_timer_now()
    trans_shares = tradesql_get_minute_amount_by_date(stock_id, now)
    if trans_shares > 1:
        return True
    else:
        return False


def tradelogic_transaction_submit(stock_id, amount, price):
    #check stock status
    if tradelogic_is_bargaining(stock_id) is False:
        log_trade.info("tradelogic: %s is NOT in bargaining!", stock_id)
        return None
    #check price
    if price > 0:
        pass
    else:
        log_trade.error("tradelogic: the price %f of %s is INVALID!", price, stock_id)
        return None
    now = back_get_timer_now()
    order_id = __tradelogic_get_order_id__()
    """the judgement of whether transaction is deal:
        condition1: submite price is between the top and the low price
        condition2: the amount is less than 10% of all 1 minute amount"""
    top_price = tradesql_get_minute_top_price_by_date(stock_id, now)
    low_price = tradesql_get_minute_low_price_by_date(stock_id, now)
    minute_amount = tradesql_get_minute_amount_by_date(stock_id, now)
    if math.abs(amount) <= minute_amount*0.1:
        if (price > low_price) and (price < top_price):
            tradelogic_set_order_status(order_id, OrderStatus["Deal"])
        else:
            tradelogic_set_order_status(order_id, OrderStatus["Submit"])
    else:
        tradelogic_set_order_status(order_id, OrderStatus["Submit"])
    return order_id


def tradelogic_delete_order(order_id):
    status = tradelogic_get_order_status(order_id)
    if status == OrderStatus["Submit"]:
        tradelogic_set_order_status(order_id, OrderStatus["Cancel"])
        log_trade.info("tradelogic: order_id: %s Deleted", order_id)
        return True
    else:
        log_trade.info("tradelogic: order_id: %s is in status %d, can NOT Delete", order_id, status)
        return False
