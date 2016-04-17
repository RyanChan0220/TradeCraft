__author__ = 'ryan'

from LogSys.log import Logger
import datetime
from TradeSys.TradeLogic import tradelogic_cycle


log_backtest = Logger().get_logger("backtest", 1)


class BackTestGV(object):
    Test_Timer_Start = datetime.datetime.strptime("2016-01-01;09:30", "%Y-%d-%m;%H:%M")
    Test_Timer_Now = Test_Timer_Start
    Test_Timer_End = datetime.datetime.strptime("2016-01-02;09:30", "%Y-%d-%m;%H:%M")
    Test_Cycle = 0


def back_get_timer_now():
    return BackTestGV.Test_Timer_Now


def back_timer_add():
    BackTestGV.Test_Timer_Now = BackTestGV.Test_Timer_Now + datetime.timedelta(minutes=1)
    if BackTestGV.Test_Timer_Now.hour >= 15 and BackTestGV.Test_Timer_Now.minute > 00:
        BackTestGV.Test_Timer_Now = BackTestGV.Test_Timer_Now + datetime.timedelta(hours=18, minutes=30)
    elif (BackTestGV.Test_Timer_Now.hour >= 11 and BackTestGV.Test_Timer_Now.minute > 30) \
            and (BackTestGV.Test_Timer_Now.hour < 13):
        BackTestGV.Test_Timer_Now = BackTestGV.Test_Timer_Now + datetime.timedelta(hours=1, minutes=29)


def back_get_start_time():
    return BackTestGV.Test_Timer_Start


def back_get_end_time():
    return BackTestGV.Test_Timer_End


def back_test_cycle():
    log_backtest.info("----------Cycle: %d------------Time: %s" % (BackTestGV.Test_Cycle,
                                                                   str(BackTestGV.Test_Timer_Now)))
    back_timer_add()
    BackTestGV.Test_Cycle += 1



if __name__ == '__main__':
    while BackTestGV.Test_Timer_Now <= BackTestGV.Test_Timer_End:
        tradelogic_cycle(BackTestGV.Test_Timer_Now)
        back_test_cycle()
    log_backtest.info("--------------BackTest End----------------")