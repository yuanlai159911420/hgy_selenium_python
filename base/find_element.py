from util.read_ini import ReadIni
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from typing import List


class FindElement(object):
    def __init__(self, driver, ini_path, node):
        """
        构造函数
        :param driver:
        :param ini_path:
        :param node:
        """
        self.__driver = driver
        self.__read_ini = ReadIni(ini_path, node)

    def get_element(self, key, element: WebElement = None) -> WebElement | None:
        """
        获取WebElement对象
        :param key:
        :param element: 在需要传入一个element时就使用该变量
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]
        """判断是否传入了element对象"""
        element = self.__driver if element is None else element

        try:
            """判断by值"""
            if by == "id":
                return element.find_element(By.ID, value)
            elif by == "className":
                return element.find_element(By.CLASS_NAME, value)
            elif by == "name":
                return element.find_element(By.NAME, value)
            elif by == "css":
                return element.find_element(By.CSS_SELECTOR, value)
            elif by == "link":
                return element.find_element(By.LINK_TEXT, value)
            elif by == "linkText":
                return element.find_element(By.PARTIAL_LINK_TEXT, value)
            elif by == "tag":
                return element.find_element(By.TAG_NAME, value)
            else:
                return element.find_element(By.XPATH, value)
        except NoSuchElementException:
            return None

    def get_elements(self, key, element: WebElement = None) -> List[WebElement] | None:
        """
        获取WebElement列表对象
        :param key:
        :param element:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]
        """判断是否传入了element对象"""
        element = self.__driver if element is None else element

        try:
            if by == "id":
                return element.find_elements(By.ID, value)
            elif by == "name":
                return element.find_elements(By.NAME, value)
            elif by == "className":
                return element.find_elements(By.CLASS_NAME, value)
            elif by == "css":
                return element.find_elements(By.CSS_SELECTOR, value)
            elif by == "link":
                return element.find_elements(By.LINK_TEXT, value)
            elif by == "linkText":
                return element.find_elements(By.PARTIAL_LINK_TEXT, value)
            elif by == "tag":
                return element.find_elements(By.TAG_NAME, value)
            else:
                return element.find_elements(By.XPATH, value)
        except NoSuchElementException:
            return None

    def get_presence_element(self, key) -> WebElement | None:
        """
        等待获取WebElement对象，只要dom树结构加载完成就行
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]
        """等待对象"""
        wait = WebDriverWait(self.__driver, 20)

        try:
            if by == "id":
                return wait.until(EC.presence_of_element_located((By.ID, value)))
            elif by == "name":
                return wait.until(EC.presence_of_element_located((By.NAME, value)))
            elif by == "className":
                return wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif by == "css":
                return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
            elif by == "link":
                return wait.until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            elif by == "linkText":
                return wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
            elif by == "tag":
                return wait.until(EC.presence_of_element_located((By.TAG_NAME, value)))
            else:
                return wait.until(EC.presence_of_element_located((By.XPATH, value)))
        except NoSuchElementException:
            return None

    def get_visibility_element(self, key) -> WebElement | None:
        """
        等待获取WebElement对象，表示元素非隐藏，宽高都不是0
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]
        """创建等待元素"""
        wait = WebDriverWait(self.__driver, 20)
        try:
            if by == "id":
                return wait.until(EC.visibility_of_element_located((By.ID, value)))
            elif by == "name":
                return wait.until(EC.visibility_of_element_located((By.NAME, value)))
            elif by == "className":
                return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, value)))
            elif by == "css":
                return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
            elif by == "link":
                return wait.until(EC.visibility_of_element_located((By.LINK_TEXT, value)))
            elif by == "linkText":
                return wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))
            elif by == "tag":
                return wait.until(EC.visibility_of_element_located((By.TAG_NAME, value)))
            else:
                return wait.until(EC.visibility_of_element_located((By.XPATH, value)))
        except NoSuchElementException:
            return None

    def get_clickable_element(self, key) -> WebElement | None:
        """
        等待获取WebElement对象，需要元素在页面可以点击
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]
        """创建等待对象"""
        wait = WebDriverWait(self.__driver, 20)

        try:
            if by == "id":
                return wait.until(EC.element_to_be_clickable((By.ID, value)))
            elif by == "name":
                return wait.until(EC.element_to_be_clickable((By.NAME, value)))
            elif by == "className":
                return wait.until(EC.element_to_be_clickable((By.CLASS_NAME, value)))
            elif by == "css":
                return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, value)))
            elif by == "link":
                return wait.until(EC.element_to_be_clickable((By.LINK_TEXT, value)))
            elif by == "linkText":
                return wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, value)))
            elif by == "tag":
                return wait.until(EC.element_to_be_clickable((By.TAG_NAME, value)))
            else:
                return wait.until(EC.element_to_be_clickable((By.XPATH, value)))
        except NoSuchElementException:
            return None

    def get_above_element(self, element: WebElement, key) -> WebElement | None:
        """
        获取某个元素上面的元素，上面指的是页面上显示的上面
        :param element:
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]

        try:
            if by == "id":
                return self.__driver.find_element(locate_with(By.ID, value).above(element))
            elif by == "name":
                return self.__driver.find_element(locate_with(By.NAME, value).above(element))
            elif by == "className":
                return self.__driver.find_element(locate_with(By.CLASS_NAME, value).above(element))
            elif by == "css":
                return self.__driver.find_element(locate_with(By.CSS_SELECTOR, value).above(element))
            elif by == "link":
                return self.__driver.find_element(locate_with(By.LINK_TEXT, value).above(element))
            elif by == "linkText":
                return self.__driver.find_element(locate_with(By.PARTIAL_LINK_TEXT, value).above(element))
            elif by == "tag":
                return self.__driver.find_element(locate_with(By.TAG_NAME, value).above(element))
            else:
                return self.__driver.find_element(locate_with(By.XPATH, value).above(element))
        except NoSuchElementException:
            return None

    def get_below_element(self, element: WebElement, key) -> WebElement | None:
        """
        获取某个元素下面的元素，下面指的是页面可见的下面
        :param element:
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]

        try:
            if by == "id":
                return self.__driver.find_element(locate_with(By.ID, value).below(element))
            elif by == "name":
                return self.__driver.find_element(locate_with(By.NAME, value).below(element))
            elif by == "className":
                return self.__driver.find_element(locate_with(By.CLASS_NAME, value).below(element))
            elif by == "css":
                return self.__driver.find_element(locate_with(By.CSS_SELECTOR, value).below(element))
            elif by == "link":
                return self.__driver.find_element(locate_with(By.CSS_SELECTOR, value).below(element))
            elif by == "linkText":
                return self.__driver.find_element(locate_with(By.PARTIAL_LINK_TEXT, value).below(element))
            elif by == "tag":
                return self.__driver.find_element(locate_with(By.TAG_NAME, value).below(element))
            else:
                return self.__driver.find_element(locate_with(By.XPATH, value).below(element))
        except NoSuchElementException:
            return None

    def get_right_element(self, element: WebElement, key) -> WebElement | None:
        """
        获取某个元素右边的元素，右边指的是页面可见的右边
        :param element:
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]

        try:
            if by == "id":
                return self.__driver.find_element(locate_with(By.ID, value).to_right_of(element))
            elif by == "name":
                return self.__driver.find_element(locate_with(By.NAME, value).to_right_of(element))
            elif by == "className":
                return self.__driver.find_element(locate_with(By.CLASS_NAME, value).to_right_of(element))
            elif by == "css":
                return self.__driver.find_element(locate_with(By.CSS_SELECTOR, value).to_right_of(element))
            elif by == "link":
                return self.__driver.find_element(locate_with(By.LINK_TEXT, value).to_right_of(element))
            elif by == "linkText":
                return self.__driver.find_element(locate_with(By.PARTIAL_LINK_TEXT, value).to_right_of(element))
            elif by == "tag":
                return self.__driver.find_element(locate_with(By.TAG_NAME, value).to_right_of(element))
            else:
                return self.__driver.find_element(locate_with(By.XPATH, value).to_right_of(element))
        except NoSuchElementException:
            return None

    def get(self, element: WebElement, key) -> WebElement | None:
        """
        获取某个元素左边的元素，左边指的是页面可见的左边
        :param element:
        :param key:
        :return:
        """
        """获取数据"""
        data = self.__read_ini.get_data(key)
        """拆分数据"""
        by = data.split("->")[0]
        value = data.split("->")[1]

        try:
            if by == "id":
                return self.__driver.find_element(locate_with(By.ID, value).to_left_of(element))
            elif by == "name":
                return self.__driver.find_element(locate_with(By.NAME, value).to_left_of(element))
            elif by == "className":
                return self.__driver.find_element(locate_with(By.CLASS_NAME, value).to_left_of(element))
            elif by == "css":
                return self.__driver.find_element(locate_with(By.CSS_SELECTOR, value).to_left_of(element))
            elif by == "link":
                return self.__driver.find_element(locate_with(By.LINK_TEXT, value).to_left_of(element))
            elif by == "linkText":
                return self.__driver.find_element(locate_with(By.PARTIAL_LINK_TEXT, value).to_left_of(element))
            elif by == "tag":
                return self.__driver.find_element(locate_with(By.TAG_NAME, value).to_left_of(element))
            else:
                return self.__driver.find_element(locate_with(By.XPATH, value).to_left_of(element))
        except NoSuchElementException:
            return None
