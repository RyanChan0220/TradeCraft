__author__ = 'ryan'

import logging
import logging.config


# logging.config.fileConfig('..\\LogSys\\logger.conf')
# print_log = logging.getLogger('root')
# file_log = logging.getLogger('fileLogger')


class Logger(object):
    Logger = {}
    Logger_count = 0

    def __init__(self):
        pass

    def get_logger(self, log_name, log_type):
        log_tmp = logging.getLogger(log_name)
        log_tmp.setLevel(logging.INFO)
        if log_type == 0:
            log_handler = logging.StreamHandler()
        else:
            log_handler = logging.FileHandler("..\\LogSys\\" + log_name + ".log")
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        log_tmp.addHandler(log_handler)
        self.Logger[log_name] = log_tmp
        self.Logger_count += 1
        return self.Logger[log_name]