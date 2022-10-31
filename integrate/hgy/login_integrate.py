from handle.hgy.login_handle import LoginHandle
import os


class LoginIntegrate(object):
    def __init__(self, driver):
        """
        构造函数:
            ::核工业登陆页面集成操作
        :param driver:
        """
        __ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                  "config/hgy/login_config.ini")
        __node = "LoginConfig"
        self.__login_hd = LoginHandle(driver, __ini_path, __node)

    def send_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        key = "username"
        self.__login_hd.send_username(key, username)

    def send_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        key = "password"
        self.__login_hd.send_password(key, password)

    def click_login_button(self):
        """
        点击登陆按钮
        :return:
        """
        key = "login_button"
        self.__login_hd.click_login_button(key)

    def click_radio_gly(self):
        """
        选择业务管理云
        :return:
        """
        key = "radio_gly"
        self.__login_hd.click_radio(key)

    def click_radio_xty(self):
        """
        选择勘察协同云
        :return:
        """
        key = "radio_xty"
        self.__login_hd.click_radio(key)

    def click_radio_yty(self):
        """
        选择岩土分析云
        :return:
        """
        key = "radio_yty"
        self.__login_hd.click_radio(key)

    def login_gly(self, username, password):
        """
        登陆业务管理云
        :param username:
        :param password:
        :return:
        """
        self.send_username(username)
        self.send_password(password)
        self.click_radio_gly()
        self.click_login_button()

    def login_xty(self, username, password):
        """
        登陆勘察协同云
        :param username:
        :param password:
        :return:
        """
        self.send_username(username)
        self.send_password(password)
        self.click_radio_xty()
        self.click_login_button()

    def login_yty(self, username, password):
        """
        登陆岩土分析云
        :param username:
        :param password:
        :return:
        """
        self.send_username(username)
        self.send_password(password)
        self.click_radio_yty()
        self.click_login_button()


if __name__ == '__main__':
    login_ig = LoginIntegrate("123")
