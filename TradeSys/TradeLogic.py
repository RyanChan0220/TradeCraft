__author__ = 'ryan'

import collections
from TradeSys.TradeSQL import *
from LogSys.log import Logger
import datetime
import math

OrderStatus = {"Empty": 0, "Deal": 1, "Submit": 2, "Cancel": 3}

log_tradelogic = Logger().get_logger("log_tradelogic", 1)


class TradeLogicGV(object):
    Timer_Now = datetime.datetime.strptime("2007-01-01;09:30", "%Y-%m-%d;%H:%M")
    Cycle = 0
    Order_Count = 0
    Orders = collections.OrderedDict()


def tradelogic_set_now_time(now):
    TradeLogicGV.Timer_Now = now


def tradelogic_cycle(now):
    #check orders
    tradelogic_set_now_time(now)
    TradeLogicGV.Cycle += 1
    # time_now = StartTime + datetime.timedelta(minutes=tradelogic_cycle.count)
    log_tradelogic.info("tradelogic Cycle %s" % TradeLogicGV.Cycle)


def tradelogic_get_order_status(order_id):
    if order_id in TradeLogicGV.Orders:
        return TradeLogicGV.Orders[order_id]
    else:
        return OrderStatus["Empty"]


def tradelogic_set_order_status(order_id, status=OrderStatus["Empty"]):
    if order_id in TradeLogicGV.Orders:
        TradeLogicGV.Orders[order_id] = status
    else:
        pass


def __tradelogic_get_order_id__():
    TradeLogicGV.Order_Count += 1
    TradeLogicGV.Orders[TradeLogicGV.Order_Count] = OrderStatus["Empty"]
    return TradeLogicGV.Order_Count


def tradelogic_get_price(stock_id):
    if tradelogic_is_bargaining(stock_id) is True:
        price = tradesql_get_minute_open_price_by_date(stock_id, TradeLogicGV.Timer_Now)
    else:
        price = 0
    return price


def tradelogic_is_bargaining(stock_id):
    trans_shares = tradesql_get_minute_amount_by_date(stock_id, TradeLogicGV.Timer_Now)
    if trans_shares > 1:
        return True
    else:
        return False


def tradelogic_transaction_submit(stock_id, amount, price):
    #check stock status
    if tradelogic_is_bargaining(stock_id) is False:
        log_tradelogic.info("tradelogic: %s is NOT in bargaining!", stock_id)
        return None
    #check price
    if price > 0:
        pass
    else:
        log_tradelogic.error("tradelogic: the price %f of %s is INVALID!", price, stock_id)
        return None
    order_id = __tradelogic_get_order_id__()
    """the judgement of whether transaction is deal:
        condition1: submite price is between the top and the low price
        condition2: the amount is less than 10% of all 1 minute amount"""
    top_price = tradesql_get_minute_top_price_by_date(stock_id, TradeLogicGV.Timer_Now)
    low_price = tradesql_get_minute_low_price_by_date(stock_id, TradeLogicGV.Timer_Now)
    minute_amount = tradesql_get_minute_amount_by_date(stock_id, TradeLogicGV.Timer_Now)
    if math.fabs(amount) <= minute_amount*0.1:
        if (price >= low_price) and (price <= top_price):
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
        log_tradelogic.info("tradelogic: order_id: %s Deleted", order_id)
        return True
    else:
        log_tradelogic.info("tradelogic: order_id: %s is in status %d, can NOT Delete", order_id, status)
        return False
