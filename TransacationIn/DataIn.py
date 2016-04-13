from TransacationIn import TxtIn
from LogSys.log import Logger
from TradeSys.TradeLogic import *
from BackTestSys.BackTest import *
import datetime

__author__ = 'ryan'

if __name__ == '__main__':
    now = back_get_timer_now()
    print now
    date = now + datetime.timedelta(days=-300)
    print date
    ret = tradesql_get_daily_close_price_by_date("sz000002", date)
    print ret
    # txt2db = TxtIn.TXT2DB()
    # txt2db.daily2db_multi()
    # file_log = Logger()
    # log = file_log.get_logger("testlog", 1)
    # log.info("test")
    # log2 = file_log.get_logger("testlog2", 1)
    # log2.info("test2")