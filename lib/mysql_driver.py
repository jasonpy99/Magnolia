# coding: utf-8
import mysql.connector
from config import *


class MysqlDriver(object):
    def __init__(self):
        self.cnn = mysql.connector.connect(**MYSQLCONFIG)
        self.cursor = self.cnn.cursor()
        pass

    def put(self, query, query_dict):
        """
        上传
        :param query: sql语句
        :param query_dict: 参数
        """
        self.cursor.execute(query, query_dict)
        self.cnn.commit()

    def close(self):
        self.cursor.close()
        self.cnn.close()

    def fetch(self, query):
        """
        获取
        :param query: sql语句
        :return:
        """
        result = []
        self.cursor.execute(query)
        for item in self.cursor:
            result.append(item)
        return result

