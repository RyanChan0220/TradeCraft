__author__ = 'ryan'
from datetime import datetime

Test_Timer_Start = datetime.today()
Test_Timer_Now = datetime.today()
Test_Timer_End = datetime.today()


def back_get_timer_now():
    return Test_Timer_Now


def back_get_start_time():
    return Test_Timer_Start


def back_get_end_time():
    return Test_Timer_End