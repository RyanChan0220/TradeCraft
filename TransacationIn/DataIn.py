from TransacationIn import TxtIn
from LogSys.log import Logger

__author__ = 'ryan'

if __name__ == '__main__':
    # txt2db = TxtIn.TXT2DB()
    # txt2db.daily2db_multi()
    file_log = Logger()
    log = file_log.get_logger("testlog", 1)
    log.info("test")
    log2 = file_log.get_logger("testlog2", 1)
    log2.info("test2")