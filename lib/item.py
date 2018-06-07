# coding: utf-8


class Item(object):
    """数据"""
    def __init__(self):
        self.page_source = None
        self.key = None
        pass


class ItemPage(Item):
    """单个网页的详细信息"""
    def __init__(self):
        super(ItemPage, self).__init__()
        self.num = None


class ItemGood(Item):
    """单个商品的详细信息"""
    def __init__(self):
        super(ItemGood, self).__init__()
        self.id = None

