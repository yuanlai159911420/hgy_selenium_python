from base.find_element import FindElement
from selenium.webdriver.remote.webdriver import WebElement


class LoginPage(object):
    def __init__(self, driver, ini_path, node):
        """
        构造函数
            ::登陆页面元素获取，初始化对象
        :param driver:
        :param ini_path:
        :param node:
        """
        self.__find_element = FindElement(driver, ini_path, node)

    def get_username_element(self, key) -> WebElement:
        """
        获取用户名对象
        :param key:
        :return:
        """
        return self.__find_element.get_visibility_element(key)

    def get_password_element(self, key) -> WebElement:
        """
        获取密码对象
        :param key:
        :return:
        """
        return self.__find_element.get_element(key)

    def get_login_button_element(self, key) -> WebElement:
        """
        获取登录按钮对象
        :param key:
        :return:
        """
        return self.__find_element.get_element(key)

    def get_radio_element(self, key) -> WebElement:
        """
        获取radio按钮对象
        :param key:
        :return:
        """
        return self.__find_element.get_element(key)
