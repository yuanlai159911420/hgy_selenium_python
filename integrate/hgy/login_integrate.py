from handle.hgy.login_handle import LoginHandle
import os


class LoginIntegrate(object):
    def __init__(self, driver):
        """

        :param driver:
        """
        __ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                  "config/hgy/login_config.ini")
        __node = "LoginConfig"
        self.__login_hd = LoginHandle(driver, __ini_path, __node)


if __name__ == '__main__':
    login_ig = LoginIntegrate("123")
