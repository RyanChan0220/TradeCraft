__author__ = 'ryan'

OrderType = {"Market": 0, "Limit": 1}

#InFunc 获取一个订单号
@staticmethod
def trade_get_order_id():
    pass
    return 0


#OutFunc 获取当前订单状态，0代表未成交，1代表成交
def trade_get_order_status(order_id):
    return 0


def trade_order_shares(id, amount, style = OrderType["Market"]):
    order_id = trade_get_order_id()
    pass
    return order_id


def trade_order_lots(id, amount, style = OrderType["Market"]):
    order_id = trade_get_order_id()
    pass
    return order_id


def trade_order_value(id, cash_amount, style = OrderType["Market"]):
    order_id = trade_get_order_id()
    pass
    return order_id


def trade_order_percent(id, percent, style = OrderType["Market"]):
    order_id = trade_get_order_id()
    pass
    return order_id


def trade_order_target_value(id, target_cash, style = OrderType["Market"]):
    order_id = trade_get_order_id()
    pass
    return order_id


def trade_order_target_percent(id, target_percent, style = OrderType["Market"]):
    order_id = trade_get_order_id()
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

