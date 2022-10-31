from integrate.hgy.login_integrate import LoginIntegrate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestLoginCase(object):
    def setup(self):
        """
        每个function前执行一次
        :return:
        """
        url = "http://www.wxt.plus:50037/auth/login"
        options = Options()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(url)

    def teardown(self):
        """
        每个function后面执行一次
        :return:
        """
        pass
        # self.driver.close()

    @pytest.mark.parametrize("username,password", [("18382115883", "123456abc.")])
    def test_case_001(self, username, password):
        login_ig = LoginIntegrate(self.driver)
        login_ig.login_gly(username, password)


if __name__ == '__main__':
    pytest.main(["-vs", "./test_login_case.py::TestLoginCase::test_case_001"])
