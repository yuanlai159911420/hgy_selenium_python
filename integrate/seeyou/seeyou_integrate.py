from handle.seeyou.seeyou_handle import SeeyouHandle
import os


class SeeyouIntegrate(object):
    def __init__(self, driver):
        """
        seeyou系统首页元素操作集成
        构造函数:
            ::初始化对象
        :param driver:
        """
        __ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                  "config/seeyou/seeyou_config.ini")
        __node = "SeeyouConfig"
        self.__seeyou_hd = SeeyouHandle(driver, __ini_path, __node)

    def click_settingIco(self):
        """
        点击settingIco设置按钮
        :return:
        """
        key = "settingIco"
        self.__seeyou_hd.click_settingIco(key)

    def click_logout(self):
        """
        点击personContainer元素中的logout退出按钮
        :return:
        """
        key = ""
        self.__seeyou_hd.click_personContainer(key)

    def click_collaborative_menu(self):
        """
        点击协同工作菜单按钮
        :return:
        """
        key = "collaborative_menu"
        self.__seeyou_hd.click_navTitleName(key)

    def click_collaborative_sent_menu(self):
        """
        点击已发事项菜单按钮
        :return:
        """
        key = "collaborative_sent_menu"
        self.__seeyou_hd.click_navTitleName(key)

    def click_collaborative_pending_menu(self):
        """
        点击待办事项菜单按钮
        :return:
        """
        key = "collaborative_pending_menu"
        self.__seeyou_hd.click_navTitleName(key)

    def click_project_filing_menu(self):
        """
        点击项目备案管理菜单按钮
        :return:
        """
        key = "project_filing_menu"
        self.__seeyou_hd.click_navTitleName(key)

    def click_project_filing_main_menu(self):
        """
        点击项目备案登记表菜单按钮
        :return:
        """
        key = "project_filing_main_menu"
        self.__seeyou_hd.click_navTitleName(key)


if __name__ == '__main__':
    seeyou_ig = SeeyouIntegrate("123")
