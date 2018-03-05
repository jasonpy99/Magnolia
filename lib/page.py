# coding: utf-8
# created by: 'sunan'
# created at: '2018/3/4 下午4:02'


class Page(object):
    """对爬取下来的网页进行处理"""
    def __init__(self):
        pass

    def extract(self):
        """具体处理该网页的方法"""
        raise NotImplementedError


class PageGoods(Page):
    """输入关键字搜索后包含多个商品的页面"""
    def __init__(self):
        super(PageGoods, self).__init__()

    def extract(self):
        pass


class PageDetail(Page):
    """单个商品的具体页面"""
    def __init__(self):
        pass

    def extract(self):
        pass
