__author__ = 'ryan'

from TradeLogic import *
from CraftSys.CraftEnv import START_MONEY

total_money = START_MONEY

OrderType = {"Market": 0, "Limit": 1}



def trade_get_now_money():
    return total_money


def trade_is_money_enough(need):
    if need < total_money:
        return True
    else:
        return False


def trade_use_money(money):
    global total_money
    if trade_is_money_enough(money) is True:
        total_money -= money
        ret = True
    else:
        #log
        ret = False
    return ret


def trade_back_money(money):
    global total_money
    total_money += money
    return True


def trade_get_name_by_id(id):
    pass


def trade_id2stockid(id):
    pass
    return 0


def trade_is_stock_id_valid(stock_id):
    pass


#OutFunc 获取当前订单状态，0代表未成交，1代表成交
def trade_get_order_status(order_id):
    return 0


def trade_order_shares(id, amount, style=OrderType["Market"], limit_price=0):
    stock_id = trade_id2stockid(id)

    #check id
    if trade_is_stock_id_valid(stock_id) is False:
        #LOG
        return OrderStatus["Cancel"]
    #check amount
    if (amount % 100) != 0:
        #LOG
        return OrderStatus["Cancel"]

    if style == OrderType["Market"]:
        price = tradelogic_get_price(stock_id)
    else:
        price = limit_price

    #check money
    need_money = price*amount
    if trade_is_money_enough(need_money) is False:
        return OrderStatus["Cancel"]

    #get order id
    order_id = tradelogic_get_order_id()
    status = tradelogic_transaction_submit(order_id, stock_id, amount, price)
    if status == OrderStatus["Dealed"]:
        trade_use_money(need_money)
    elif status == OrderStatus["Submited"]:
        pass
    return order_id


def trade_order_lots(id, amount, style = OrderType["Market"], limit_price=0):
    order_id = tradelogic_get_order_id()
    pass
    return order_id


def trade_order_value(id, cash_amount, style = OrderType["Market"], limit_price=0):
    order_id = tradelogic_get_order_id()
    pass
    return order_id


def trade_order_percent(id, percent, style = OrderType["Market"], limit_price=0):
    order_id = tradelogic_get_order_id()
    pass
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

