from base.find_element import FindElement


class SeeyouPage(object):
    def __init__(self, driver, ini_path, node):
        """
        构造函数:
            ::初始化对象
        :param driver:
        :param ini_path:
        :param node:
        """
        self.find_element = FindElement(driver, ini_path, node)

    def get_navTitleName_element(self, key):
        """
        获取首页navTitleName菜单栏对象
        :param key:
        :return:
        """
        return self.find_element.get_clickable_element(key)
