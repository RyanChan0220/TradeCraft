__author__ = 'ryan'

from LogSys.log import Logger
import datetime
from TradeSys.TradeLogic import tradelogic_cycle


log_backtest = Logger().get_logger("backtest", 1)


class GlobalVariables(object):
    Test_Timer_Start = datetime.datetime.strptime("2016-01-01;09:30", "%Y-%d-%m;%H:%M")
    Test_Timer_Now = Test_Timer_Start
    Test_Timer_End = datetime.datetime.strptime("2016-01-02;09:30", "%Y-%d-%m;%H:%M")
    Test_Cycle = 0


def back_get_timer_now():
    return GlobalVariables.Test_Timer_Now


def back_timer_add():
    GlobalVariables.Test_Timer_Now = GlobalVariables.Test_Timer_Now + datetime.timedelta(minutes=1)
    if GlobalVariables.Test_Timer_Now.hour >= 15 and GlobalVariables.Test_Timer_Now.minute > 00:
        GlobalVariables.Test_Timer_Now = GlobalVariables.Test_Timer_Now + datetime.timedelta(hours=18, minutes=30)
    elif (GlobalVariables.Test_Timer_Now.hour >= 11 and GlobalVariables.Test_Timer_Now.minute > 30) \
            and (GlobalVariables.Test_Timer_Now.hour < 13):
        GlobalVariables.Test_Timer_Now = GlobalVariables.Test_Timer_Now + datetime.timedelta(hours=1, minutes=29)


def back_get_start_time():
    return GlobalVariables.Test_Timer_Start


def back_get_end_time():
    return GlobalVariables.Test_Timer_End


def back_test_cycle():
    log_backtest.info("----------Cycle: %d------------Time: %s" % (GlobalVariables.Test_Cycle,
                                                                   str(GlobalVariables.Test_Timer_Now)))
    back_timer_add()
    GlobalVariables.Test_Cycle += 1



if __name__ == '__main__':
    while GlobalVariables.Test_Timer_Now <= GlobalVariables.Test_Timer_End:
        tradelogic_cycle(GlobalVariables.Test_Timer_Now)
        back_test_cycle()
    log_backtest.info("--------------BackTest End----------------")