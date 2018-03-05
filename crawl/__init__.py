# coding: utf-8
# created by: 'sunan'
# created at: '2018/3/5 下午12:59'

from lib.selenium_driver import SeleniumDriver

selenium = SeleniumDriver('/Users/sunan/ENV_package/magnolia/lib/python3.5/chromedriver')
selenium.search('硬纸箱', 2)