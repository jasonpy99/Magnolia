# coding: utf-8
# created by: 'sunan'
# created at: '2018/3/5 下午5:16'

from lib.selenium_driver import SeleniumDriver
from config import *


if __name__ == '__main__':
    a = SeleniumDriver(CHROMEDRIVER)
    a.search('硬纸箱', 100)
