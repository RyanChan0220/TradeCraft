from TransacationIn import TxtIn
from LogSys.log import Logger
from TradeSys.TradeLogic import *
from BackTestSys.BackTest import *
import datetime
from TransacationIn.downloadTrans import DownloadTrans
from TransacationIn.trans2DB import Trans2DB

__author__ = 'ryan'

if __name__ == '__main__':
    tradelogic_cycle()
    date = datetime.datetime.strptime("2015-05-04 09:35", "%Y-%m-%d %H:%M")
    print date
    ret = tradesql_get_minute_low_price_by_date("sh600000", date)
    print ret
    # txt2db = TxtIn.TXT2DB("minute")
    # txt2db.daily2db_multi()
    # txt2db.minute2db_multi()
    # dt = DownloadTrans()
    # dt.download_multi()
    # trans_handler = Trans2DB("trans", "D:\\StockData\\trans")
    # trans_handler.trans_db_multi()