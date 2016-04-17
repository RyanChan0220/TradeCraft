__author__ = 'ryan'

import collections
from TradeSys.TradeSQL import *
from TradeFunc import log_trade
import datetime
import math

OrderStatus = {"Empty": 0, "Deal": 1, "Submit": 2, "Cancel": 3}
Orders = collections.OrderedDict()


class GlobalVariables(object):
    Timer_Now = datetime.datetime.strptime("2007-01-01;09:30", "%Y-%d-%m;%H:%M")
    Cycle = 0
    Order_Count = 0


def tradelogic_set_now_time(now):
    GlobalVariables.Timer_Now = now


def tradelogic_cycle(now):
    #check orders
    tradelogic_set_now_time(now)
    GlobalVariables.Cycle += 1
    # time_now = StartTime + datetime.timedelta(minutes=tradelogic_cycle.count)
    log_trade.info("tradelogic Cycle %s" % GlobalVariables.Cycle)


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
    GlobalVariables.Order_Count += 1
    return __tradelogic_get_order_id__.count


def tradelogic_get_price(stock_id):
    price = tradesql_get_minute_open_price_by_date(stock_id, GlobalVariables.Timer_Now)
    return price


def tradelogic_is_bargaining(stock_id):
    trans_shares = tradesql_get_minute_amount_by_date(stock_id, GlobalVariables.Timer_Now)
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
    order_id = __tradelogic_get_order_id__()
    """the judgement of whether transaction is deal:
        condition1: submite price is between the top and the low price
        condition2: the amount is less than 10% of all 1 minute amount"""
    top_price = tradesql_get_minute_top_price_by_date(stock_id, GlobalVariables.Timer_Now)
    low_price = tradesql_get_minute_low_price_by_date(stock_id, GlobalVariables.Timer_Now)
    minute_amount = tradesql_get_minute_amount_by_date(stock_id, GlobalVariables.Timer_Now)
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
