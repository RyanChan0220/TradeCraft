__author__ = 'ryan'

from Frameworks.MySQL import *

daily_db = MySQL("daily")
minute_db = MySQL("minute")


def tradesql_get_daily_close_price_by_date(sqlid, date):
    daily_db.connect()
    condition = "DATE='%s'" % date.strftime("%Y-%m-%d")
    print condition
    ret = daily_db.query_where(sqlid, condition)
    daily_db.close_connect()
    if len(ret) is 0:
        return None
    else:
        return ret[0][5]


def tradesql_get_daily_open_price_by_date(sqlid, date):
    daily_db.connect()
    condition = "DATE='%s'" % date.strftime("%Y-%m-%d")
    print condition
    ret = daily_db.query_where(sqlid, condition)
    daily_db.close_connect()
    if len(ret) is 0:
        return None
    else:
        return ret[0][2]


def tradesql_get_daily_top_price_by_date(sqlid, date):
    daily_db.connect()
    condition = "DATE='%s'" % date.strftime("%Y-%m-%d")
    print condition
    ret = daily_db.query_where(sqlid, condition)
    daily_db.close_connect()
    if len(ret) is 0:
        return None
    else:
        return ret[0][3]


def tradesql_get_daily_low_price_by_date(sqlid, date):
    daily_db.connect()
    condition = "DATE='%s'" % date.strftime("%Y-%m-%d")
    print condition
    ret = daily_db.query_where(sqlid, condition)
    daily_db.close_connect()
    if len(ret) is 0:
        return None
    else:
        return ret[0][4]


def tradesql_get_minute_close_price_by_date(sqlid, date):
    minute_db.connect()
    minute_db.close_connect()


def tradesql_get_minute_open_price_by_date(sqlid, date):
    minute_db.connect()
    minute_db.close_connect()


def tradesql_get_minute_top_price_by_date(sqlid, date):
    minute_db.connect()
    minute_db.close_connect()


def tradesql_get_minute_low_price_by_date(sqlid, date):
    minute_db.connect()
    minute_db.close_connect()


#get the 1 minute amount of stock by date
def tradesql_get_minute_amount_by_date(sqlid, date):
    minute_db.connect()
    minute_db.close_connect()