# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lib.item import ItemPage
from lib.mysql_driver import MysqlDriver


class SeleniumDriver(object):
    def __init__(self, path):
        self.browser = webdriver.Chrome(path)
        # 初始化mysql_drive实例
        self.mysql_driver = MysqlDriver()

    def search(self, keyword, num):
        """
        根据特定的key来搜索宝贝，将保存前num页的源码
        :param keyword: 待搜索的关键字
        :param num: 需要爬取的商品页面数（<=100）
        """
        self.browser.get('http://www.taobao.com')
        # 找到"请输入要搜索的关键词"并点击"搜索"
        self.put_submit_by_xpath('//*[@id="q"]', '//*[@id="J_TSearchForm"]/div[1]/button', keyword)
        for i in range(1, num+1):
            # 输入"页码"并点击"确认"
            self.put_submit_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/input', '//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]', i)
            # 处理页面信息
            self.page_process(keyword, i)
        self.mysql_driver.close()

    def put_submit_by_xpath(self, input_element, submit_element, keyword, wait=10):
        """
        在input_element中填入keyword并点击submit_element按钮
        :param input_element: 需要填入字段的元素xpath
        :param submit_element: 需要点击的元素xpath
        :param keyword: 要填入的字段
        :param wait: 寻找元素等待的时间， 默认10秒
        """
        input_element = WebDriverWait(self.browser, wait).until(
            EC.presence_of_element_located((By.XPATH, input_element))
        )
        input_element.clear()
        input_element.send_keys(keyword)
        submit_element = WebDriverWait(self.browser, wait).until(
            EC.presence_of_element_located((By.XPATH, submit_element))
        )
        submit_element.click()

    def page_process(self, key, num):
        """
        处理单个页面
        :param key: 关键词
        :param num: 页面数
        :return 包含Page对象的list
        """
        page = ItemPage()
        page.page_source = self.browser.page_source
        page.key = key
        page.num = num
        sql = "insert into magnolia_page(keyword,page_source,num) values(%(keyword)s,%(page_source)s,%(num)s)"
        sql_dict = {'keyword': page.key, 'page_source': page.page_source, 'num': page.num}
        self.mysql_driver.put(sql, sql_dict)
