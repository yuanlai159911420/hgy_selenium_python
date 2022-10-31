from page.seeyou.seeyou_page import SeeyouPage


class SeeyouHandle(object):
    def __init__(self, driver, ini_path, node):
        """
        seeyou系统首页元素操作
        构造函数:
            ::初始化对象
        :param driver:
        :param ini_path:
        :param node:
        """
        self.__seeyou_pg = SeeyouPage(driver, ini_path, node)

    def click_navTitleName(self, key):
        """
        点击navTitleName导航栏图标
        :param key:
        :return:
        """
        self.__seeyou_pg.get_navTitleName_element(key).click()

    def click_settingIco(self, key):
        """
        点击settingIco设置按钮
        :param key:
        :return:
        """
        self.__seeyou_pg.get_settingIco_element(key).click()

    def click_personContainer(self, key):
        """
        点击personContainer元素
        :param key:
        :return:
        """
        self.__seeyou_pg.get_personContainer_element(key).click()
