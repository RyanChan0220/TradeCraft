__author__ = 'ryan'

import os
from os.path import join
from Frameworks.MySQL import MySQL
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
import thread

fork_processing = 1


class TXT2DB(object):
    my_lock = thread.allocate_lock()
    db_name = "daily"
    path = "C:\\new_gdzq_v6\\T0002\\export"

    def __init__(self, daily_db="daily", src_dir="C:\\new_gdzq_v6\\T0002\\export"):
        self.db_name = daily_db
        self.path = src_dir

    def daily2db_multi(self):
        pool = ThreadPool(fork_processing)
        try:
            for root, dirs, files in os.walk(self.path):
                files_low = []
                for file_name in files:
                    files_low.append(file_name.lower())
                ret = pool.map(self.daily_file2db, files_low)
        except Exception, e:
            print e
        finally:
            pool.close()
            pool.join()

    def daily_file2db(self, stock_name):
        mysql = MySQL(self.db_name)
        mysql.connect()
        if stock_name.find('.txt') == -1:
            print "%s is error file!" % stock_name
        else:
            try:
                table_name = stock_name.split('.')[0]
                full_file_name = join(self.path, stock_name)
                txt_file = open(full_file_name)
                stock_name = txt_file.readline().decode('gbk').encode('utf-8')
                # for str in stock_name.split(" ", 3):
                # print str.lstrip().rstrip()
                title = txt_file.readline().decode('gbk').encode('utf-8')
                # for str in title.lstrip().split("\t", 7):
                # print str.lstrip()
                print "Processing daily to DB File: %s" % stock_name.lstrip().rstrip()
                col_type = list()
                col_type.append("`ID` INT NOT NULL AUTO_INCREMENT")
                col_type.append("`DATE` DATETIME NULL")
                col_type.append("`OPEN` FLOAT NULL")
                col_type.append("`TOP` FLOAT NULL")
                col_type.append("`LOW` FLOAT NULL")
                col_type.append("`CLOSE` FLOAT NULL")
                col_type.append("`VOL` INT NULL")
                col_type.append("`TURN` FLOAT NULL")
                mysql.create_table_with_delete(table_name, "ID", col_type)
                content = txt_file.readline()
                data = list()
                while content:
                    content = content.replace('\n', '')
                    contents = content.split(';', 7)
                    content = txt_file.readline()
                    if len(contents) < 7:
                        continue
                    else:
                        self.my_lock.acquire()
                        contents[0] = datetime.strptime(contents[0], "%m/%d/%Y").strftime("%Y-%m-%d %H:%M:%S")
                        self.my_lock.release()
                        data.append(contents)
                mysql.insert_many(table_name, "`DATE`, `OPEN`, `TOP`, `LOW`, \
                `CLOSE`, `VOL`, `TURN`", data)
            except IOError, e:
                print "ERROR: " + e + "\tFile:" + stock_name
                raise e
        mysql.close_connect()


