__author__ = 'ryan'

from TradeLogic import *
from CraftSys.CraftEnv import START_MONEY
import math
from LogSys.log import Logger


log_trade = Logger().get_logger("log_trade", 1)

total_money = START_MONEY
OrderType = {"Market": 0, "Limit": 1}
StockAmount = {}


def trade_get_now_money():
    return total_money


def trade_get_start_money():
    return START_MONEY


def trade_is_money_enough(need):
    if need < total_money:
        return True
    else:
        return False


def trade_use_money(money):
    global total_money
    if money > 0:
        if trade_is_money_enough(money) is True:
            total_money -= money
        else:
            log_trade.info("use money: money is not enough!")
    else:
        total_money -= money


def trade_stockid2id(stock_id):
    return stock_id


def trade_id2stockid(id):
    return id


def trade_is_stock_id_valid(stock_id):
    return True


def trade_change_stock_amount(stock_id, amount):
    global StockAmount
    if stock_id in StockAmount:
        if amount >= 0:
            StockAmount[stock_id] += amount
        else:
            if StockAmount[stock_id] > math.fabs(amount):
                StockAmount[stock_id] += amount
            else:
                rest_amount = StockAmount[stock_id]
                StockAmount[stock_id] = 0
                log_trade.info("stock %s is not enough for selling, but sell all %d", stock_id, rest_amount)
                return rest_amount
    else:
        StockAmount[stock_id] = 0
        if amount >= 0:
            StockAmount[stock_id] += amount
        else:
            StockAmount[stock_id] = 0
            log_trade.error("amount must be positive because %s isn't exist", stock_id)
            return 0
    return amount


def trade_order_shares(id, shares, style=OrderType["Market"], limit_price=0):
    stock_id = trade_id2stockid(id)
    #check id
    if trade_is_stock_id_valid(stock_id) is False:
        log_trade.error("trade_order_shares: %s is not valid stock id", stock_id)
        return None
    #check amount
    if (shares % 100) != 0:
        log_trade.error("trade_order_shares: %d is not valid amount", shares)
        return None
    if style == OrderType["Market"]:
        price = tradelogic_get_price(stock_id)
    else:
        price = limit_price
    #check money
    need_money = price*shares
    if trade_is_money_enough(need_money) is False:
        return None
    #get order id
    order_id = tradelogic_get_order_id()
    status = tradelogic_transaction_submit(order_id, stock_id, shares, price)
    if status == OrderStatus["Dealed"]:
        dealed_amount = trade_change_stock_amount(stock_id, shares)
        trade_use_money(price*dealed_amount)
    elif status == OrderStatus["Submited"]:
        pass
    else:
        pass
    return order_id


def trade_order_lots(id, lots, style=OrderType["Market"], limit_price=0):
    return trade_order_shares(id, lots*100, style, limit_price)


def trade_order_value(id, cash_amount, style=OrderType["Market"], limit_price=0):
    stock_id = trade_id2stockid(id)
    #get price
    if style == OrderType["Market"]:
        price = tradelogic_get_price(stock_id)
    else:
        price = limit_price
    shares = cash_amount/price
    return trade_order_shares(id, shares, style, limit_price)


def trade_order_percent(id, percent, style = OrderType["Market"], limit_price=0):
    order_id = None
    if (percent < 1) and (percent > -1):
        all_money = trade_get_start_money()
        order_id = trade_order_value(id, all_money*percent, style, limit_price)
    else:
        log_trade.error("trade_order_percent: %d is out of range %s", percent, id)
    return order_id


def trade_order_target_value(id, target_cash, style = OrderType["Market"], limit_price=0):
    order_id = tradelogic_get_order_id()
    pass
    return order_id


def trade_order_target_percent(id, target_percent, style = OrderType["Market"], limit_price=0):
    order_id = tradelogic_get_order_id()
    pass
    return order_id


def trade_cancel_order(order_id):
    pass
    return 0


def trade_get_order(order_id):
    pass
    return order_id


def trade_get_open_orders():
    pass

