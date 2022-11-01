from page.seeyou.zwIframe_page import ZWIframePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.keys import Keys
import random


class ZWIframeHandle(object):
    def __init__(self, driver, ini_path, node):
        """
        操作zwIframe窗口中的控件基础对象，需要前置对象才能操作
        构造函数:
            ::初始化对象
        :param driver:
        :param ini_path:
        :param node:
        """
        self.__driver = driver
        self.__zwIframe_pg = ZWIframePage(self.__driver, ini_path, node)
        self.__actions = ActionChains(self.__driver)

    def toogle_zwIframe(self, key):
        """
        进入zwIframe窗口页面
        :param key:
        :return:
        """
        self.__driver.switch_to.window(self.__zwIframe_pg.get_zwIframe_element(key))

    def send_cap4_select_text(self, element: WebElement, key, expect):
        """
        输入cap4-select__text文本框
        :param element:
        :param key:
        :param expect:
        :return:
        """
        self.__actions.send_keys_to_element(self.__zwIframe_pg.get_cap4_select_text_element(element, key),
                                            expect).perform()

    def click_cap4_select_text(self, element: WebElement, key):
        """
        点击cap4-select__text文本款
        :param element:
        :param key:
        :return:
        """
        ele = self.__zwIframe_pg.get_cap4_select_text_element(element, key)
        self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()

    def click_cap4_scontent_item(self, element: WebElement, key, expect=None):
        """
        点击cap4-scontent__item选择框对象
        :param element:
        :param key:
        :param expect:
        :return:
        """
        """获取所有items对象"""
        eles = self.__zwIframe_pg.get_cap4_scontent_item_elements(element, key)
        """判断是否输入默认值"""
        if expect is not None:
            """遍历对象"""
            for ele in eles:
                if ele.text == expect:
                    """选择对象"""
                    self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()
                    break
        else:
            """随机获取一个元素"""
            ele = random.choice(eles)
            """选择对象"""
            self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()

    def send_cap4_text_cnt(self, element: WebElement, key, expect):
        """
        输入cap4-text__cnt文本框
        :param element:
        :param key:
        :param expect:
        :return:
        """
        self.__actions.send_keys_to_element(self.__zwIframe_pg.get_cap4_text_cnt_element(element, key),
                                            expect, Keys.TAB).perform()

    def click_cap4_text_relation(self, element: WebElement, key):
        """
        点击cap4-text__relation输入框picker弹窗
        :param element:
        :param key:
        :return:
        """
        ele = self.__zwIframe_pg.get_cap4_text_relation_element(element, key)
        self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()

    def click_cap4_checkbox(self, key, right_key, left_key, *args):
        """
        选择cap4-checkbox选择框
        :param key:
        :param right_key:
        :param left_key:
        :param args:
        :return:
        """
        """获取所有cap4-checkbox对象"""
        eles = self.__zwIframe_pg.get_cap4_checkbox_elements(key)
        """遍历预期值"""
        for arg in args:
            """遍历对象"""
            for ele in eles:
                if self.__zwIframe_pg.get_cap4_checkbox_left_element(ele, left_key).text == arg:
                    self.__zwIframe_pg.get_cap4_checkbox_right_element(ele, right_key).click()
                    break

    def send_cap4_people_input(self, element: WebElement, key, expect):
        """
        输入cap4-people__input输入框
        :param element:
        :param key:
        :param expect:
        :return:
        """
        self.__actions.send_keys_to_element(self.__zwIframe_pg.get_cap4_people_input_element(element, key),
                                            expect).perform()

    def click_cap4_people_picker(self, element: WebElement, key):
        """
        点击cap4-people__picker输入框picker弹窗
        :param element:
        :param key:
        :return:
        """
        ele = self.__zwIframe_pg.get_cap4_people_picker_element(element, key)
        self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()

    def send_cap4_number_cntinput(self, element: WebElement, key, expect: int):
        """
        输入cap4-number__cntinput输入框
        :param element:
        :param key:
        :param expect:
        :return:
        """
        self.__actions.send_keys_to_element(self.__zwIframe_pg.get_cap4_number_cntinput_element(element, key),
                                            expect).perform()

    def click_cap4_radio(self, element: WebElement, item_key, icon_key, text_key, expect):
        """
        选择cap4-radio单选按钮
        :param element:
        :param item_key:
        :param icon_key:
        :param text_key:
        :param expect:
        :return:
        """
        """获取item对象列表"""
        item_eles = self.__zwIframe_pg.get_cap4_radio_item_elements(element, item_key)
        """遍历对象"""
        for item_ele in item_eles:
            """判断实际值和预期值"""
            if self.__zwIframe_pg.get_cap4_radio_text_element(item_ele, text_key).text == expect:
                """选择对象"""
                ele = self.__zwIframe_pg.get_cap4_radio_icon_element(item_ele, icon_key)
                self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()
                break

    def click_cap4_field_choose_picker(self, element: WebElement, key):
        """
        点击cap4-field-choose__picker弹窗
        :param element:
        :param key:
        :return:
        """
        ele = self.__zwIframe_pg.get_cap4_field_choose_picker_element(element, key)
        self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()

    def send_cap4_textarea_cnt(self, element: WebElement, key, expect):
        """
        输入cap4-textarea__cnt输入框
        :param element:
        :param key:
        :param expect:
        :return:
        """
        self.__actions.send_keys_to_element(self.__zwIframe_pg.get_cap4_textarea_cnt_element(element, key), expect,
                                            Keys.TAB).perform()

    """toogle_RelationPage_main"""

    def toogle_RelationPage_main(self, key):
        """
        进入RelationPage_main窗口页面
        :param key:
        :return:
        """
        self.__driver.switch_to.default_content()
        self.__driver.switch_to.window(self.__zwIframe_pg.get_RelationPage_main_element(key))

    def send_cap4_condition_flex(self, element: WebElement, key, expect):
        """
        输入cap4-condition-flex输入框
        :param element:
        :param key:
        :param expect:
        :return:
        """
        self.__zwIframe_pg.get_cap4_condition_flex_element(element, key).send_keys(expect)

    def click_cap4_condition_more(self, key):
        """
        获取cap4-condition-more按钮对象
        :param key:
        :return:
        """
        self.__zwIframe_pg.get_cap4_condition_more_element(key).click()

    def click_cap4_condition_button_filter(self, key):
        """
        点击cap4-condition-button__filter筛选按钮
        :param key:
        :return:
        """
        self.__zwIframe_pg.get_cap4_condition_button_filter_element(key).click()

    def click_cap4_condition_button_reset(self, key):
        """
        点击cap4-condition-button__reset重置按钮
        :param key:
        :return:
        """
        self.__zwIframe_pg.get_cap4_condition_button_reset_element(key).click()

    def click_RelationPage_main_v_easy_table_row(self, key):
        """
        点击v-easy-table-row对象
        :param key:
        :return:
        """
        """随机选择获取一个对象"""
        ele = random.choice(self.__zwIframe_pg.get_RelationPage_main_v_easy_table_row_elements(key))
        self.__actions.scroll_to_element(ele).move_to_element(ele).click().perform()

    def click_RelationPage_main_common_button_emphasize(self, key):
        """
        点击RelationPage_main页面中的common_button_emphasize确定按钮
        :param key:
        :return:
        """
        self.__driver.switch_to.default_content()
        self.__zwIframe_pg.get_RelationPage_main_common_button_emphasize_element(key).click()

    def click_RelationPage_main_common_button_gray(self, key):
        """
        点击RelationPage_main页面中的common_button_gray取消按钮
        :param key:
        :return:
        """
        self.__driver.switch_to.default_content()
        self.__zwIframe_pg.get_RelationPage_main_common_button_gray_element(key).click()
