from handle.seeyou.zwIframe_handle import ZWIframeHandle
from selenium.webdriver.remote.webdriver import WebElement
import os


class ZWIframeIntegrate(object):
    def __init__(self, driver):
        self.__driver = driver
        __ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                  "config/seeyou/zwIframe_config.ini")
        __node = "ZWIframeConfig"
        self.__zwIframe_hd = ZWIframeHandle(self.__driver, __ini_path, __node)

    def toogle_zwIframe(self):
        """
        进入zwIframe窗口页面
        :return:
        """
        key = "zwIframe"
        self.__zwIframe_hd.toogle_zwIframe(key)

    def send_cap4_select_text(self, element: WebElement, expect):
        """
        输入cap4-select__text文本框
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_select_text"
        self.__zwIframe_hd.send_cap4_select_text(element, key, expect)

    def click_cap4_select_text(self, element):
        """
        选择cap4-select__text文本框
        :param element:
        :return:
        """
        key = "cap4_select_text"
        self.__zwIframe_hd.click_cap4_select_text(element, key)

    def click_cap4_scontent_item(self, element: WebElement, expect=None):
        """
        选择cap4-scontent__item选择框对象
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_scontent_item"
        self.__zwIframe_hd.click_cap4_scontent_item(element, key, expect)

    def send_cap4_text_cnt(self, element: WebElement, expect):
        """
        输入cap4-text__cnt文本框
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_text_cnt"
        self.__zwIframe_hd.send_cap4_text_cnt(element, key, expect)

    def click_cap4_text_relation(self, element: WebElement):
        """
        点击cap4-text__relation输入框picker弹窗
        :param element:
        :return:
        """
        key = "cap4_text_relation"
        self.__zwIframe_hd.click_cap4_text_relation(element, key)

    def click_cap4_checkbox(self, *args):
        """
        选择cap4-checkbox选择框
        :param args:
        :return:
        """
        key = "cap4_checkbox"
        right_key = "cap4_checkbox_right"
        left_key = "cap4_checkbox_left"
        self.__zwIframe_hd.click_cap4_checkbox(self.__driver, key, right_key, left_key, args)

    def send_cap4_people_input(self, element: WebElement, expect):
        """
        输入cap4-people__input输入框
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_people_input"
        self.__zwIframe_hd.send_cap4_people_input(element, key, expect)

    def click_cap4_people_picker(self, element: WebElement):
        """
        点击cap4-people__picker输入框picker弹窗
        :param element:
        :return:
        """
        key = "cap4_people_picker"
        self.__zwIframe_hd.click_cap4_people_picker(element, key)

    def send_cap4_number_cntinput(self, element: WebElement, expect: int):
        """
        输入cap4-number__cntinput输入框
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_number_cntinput"
        self.__zwIframe_hd.send_cap4_number_cntinput(element, key, expect)

    def click_cap4_radio(self, element: WebElement, expect):
        """
        选择cap4-radio单选按钮
        :param element:
        :param expect:
        :return:
        """
        item_key = "cap4_radio_item"
        icon_key = "cap4_radio_icon"
        text_key = "cap4_radio_text"
        self.__zwIframe_hd.click_cap4_radio(element, item_key, icon_key, text_key, expect)

    def click_cap4_field_choose_picker(self, element: WebElement):
        """
        点击cap4-field-choose__picker弹窗
        :param element:
        :return:
        """
        key = "cap4_field_choose_picker"
        self.__zwIframe_hd.click_cap4_field_choose_picker(element, key)

    def send_cap4_textarea_cnt(self, element: WebElement, expect):
        """
        输入cap4-textarea__cnt输入框
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_textarea_cnt"
        self.__zwIframe_hd.send_cap4_textarea_cnt(element, key, expect)

    """RelationPage_main"""

    def toogle_toogle_RelationPage_main(self):
        """
        进入RelationPage_main窗口页面
        :return:
        """
        key = "RelationPage_main"
        self.__zwIframe_hd.toogle_RelationPage_main(key)

    def send_cap4_condition_flex(self, element: WebElement, expect):
        """
        输入cap4-condition-flex输入框
        :param element:
        :param expect:
        :return:
        """
        key = "cap4_condition_flex"
        self.__zwIframe_hd.send_cap4_condition_flex(element, key, expect)

    def click_cap4_condition_button_filter(self):
        """
        点击cap4-condition-button__filter筛选按钮
        :return:
        """
        key = "cap4_condition_button_filter"
        self.__zwIframe_hd.click_cap4_condition_button_filter(key)

    def click_cap4_condition_button_reset(self):
        """
        点击cap4-condition-button__reset重置按钮
        :return:
        """
        key = "cap4_condition_button_reset"
        self.__zwIframe_hd.click_cap4_condition_button_reset(key)

    def click_RelationPage_main_v_easy_table_row(self):
        """
        选择v-easy-table-row对象
        :return:
        """
        key = "RelationPage_main_v_easy_table_row"
        self.__zwIframe_hd.click_RelationPage_main_v_easy_table_row(key)

    def click_RelationPage_main_common_button_emphasize(self):
        """
        点击RelationPage_main页面中的common_button_emphasize确定按钮
        :return:
        """
        key = "RelationPage_main_common_button_emphasize"
        self.__zwIframe_hd.click_RelationPage_main_common_button_emphasize(key)

    def click_RelationPage_main_common_button_gray(self):
        """
        点击RelationPage_main页面中的common_button_gray取消按钮
        :return:
        """
        key = "RelationPage_main_common_button_gray"
        self.__zwIframe_hd.click_RelationPage_main_common_button_gray(key)


if __name__ == '__main__':
    zwIframe_ig = ZWIframeIntegrate("123")
