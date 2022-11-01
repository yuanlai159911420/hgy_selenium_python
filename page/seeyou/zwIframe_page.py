from base.find_element import FindElement
from selenium.webdriver.remote.webdriver import WebElement
from typing import List


class ZWIframePage(object):
    def __init__(self, driver, ini_path, node):
        """
        获取zwIframe窗口页面的中控件的基础对象
        构造函数:
            ::初始化对象
        :param driver:
        :param ini_path:
        :param node:
        """
        self.__driver = driver
        self._ini_path = ini_path
        self.__node = node

    def get_zwIframe_element(self, key) -> WebElement:
        """
        获取zwIframe对象
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_presence_element(key)

    def get_cap4_select_text_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-select__text输入框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_scontent_item_elements(self, element: WebElement, key) -> List[WebElement]:
        """
        获取cap4-scontent__item选择框对象列表
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_elements(key)

    def get_cap4_text_cnt_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-text__cnt输入框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_text_relation_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-text__relation输入框relation弹窗对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_checkbox_elements(self, key) -> List[WebElement]:
        """
        获取cap4-checkbox多选框列表对象
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_elements(key)

    def get_cap4_checkbox_right_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-checkbox__right选择框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_checkbox_left_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-checkbox__left文本对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_people_input_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-people__input输入框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_people_picker_element(self, elelment: WebElement, key) -> WebElement:
        """
        获取cap4-people__picker输入框picker弹窗对象
        :param elelment:
        :param key:
        :return:
        """
        return FindElement(elelment, self._ini_path, self.__node).get_element(key)

    def get_cap4_number_cntinput_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-number__cntinput输入框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_radio_item_elements(self, element: WebElement, key) -> List[WebElement]:
        """
        获取cap4-radio__item列表对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_elements(key)

    def get_cap4_radio_icon_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-radio__icon点击按钮对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_radio_text_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-radio__text文本框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_field_choose_picker_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-field-choose__picker弹窗对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    def get_cap4_textarea_cnt_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-textarea__cnt输入框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(element, self._ini_path, self.__node).get_element(key)

    """RelationPage_main"""

    def get_RelationPage_main_element(self, key) -> WebElement:
        """
        获取RelationPage_main窗口对象
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_element(key)

    def get_cap4_condition_flex_element(self, element: WebElement, key) -> WebElement:
        """
        获取cap4-condition-flex输入框对象
        :param element:
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_right_element(element, key)

    def get_cap4_condition_more_element(self, key) -> WebElement:
        """
        获取cap4-condition-more按钮对象
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_element(key)

    def get_cap4_condition_button_filter_element(self, key) -> WebElement:
        """
        获取cap4-condition-button__filter筛选按钮对象
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_element(key)

    def get_cap4_condition_button_reset_element(self, key) -> WebElement:
        """
        获取cap4-condition-button__reset重置按钮对象
        :param key:
        :return:
        """
        return FindElement(self.__driver, self._ini_path, self.__node).get_element(key)
