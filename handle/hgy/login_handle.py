from page.hgy.login_page import LoginPage


class LoginHandle(object):
    def __init__(self, driver, ini_path, node):
        """
        构造函数:
            ::登陆页面元素操作，初始化对象
        :param driver:
        :param ini_path:
        :param node:
        """
        self.__login_pg = LoginPage(driver, ini_path, node)

    def send_username(self, key, username):
        """
        输入用户名
        :param key:
        :param username:
        :return:
        """
        self.__login_pg.get_username_element(key).send_keys(username)

    def send_password(self, key, password):
        """
        输入密码
        :param key:
        :param password:
        :return:
        """
        self.__login_pg.get_password_element(key).send_keys(password)

    def click_login_button(self, key):
        """
        点击登陆按钮
        :param key:
        :return:
        """
        self.__login_pg.get_login_button_element(key)

    def click_radio(self, key):
        """
        点击radio按钮
        :param key:
        :return:
        """
        self.__login_pg.get_radio_element(key)
