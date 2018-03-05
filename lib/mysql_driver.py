# coding: utf-8
import mysql.connector
from config import *


class MysqlDriver(object):
    def __init__(self):
        self.cnn = mysql.connector.connect(**MYSQLCONFIG)
        self.cursor = self.cnn.cursor()
        pass

    def put(self, sql, sql_dict):
        """
        上传
        :param sql: sql语句
        :param sql_dict: 参数
        """
        self.cursor.execute(sql, sql_dict)
        self.cnn.commit()

    def close(self):
        self.cursor.close()
        self.cnn.close()
