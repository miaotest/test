"""
PO基类
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=5, poll=.5):  # location存放定位到的元素，为元组类型数据
        # 添加显示等待
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))
        # return self.driver.find_element(location[0], location[1])
        return element

    # 点击操作
    def click_func(self, element):
        element.click()

    # 输入操作
    def input_func(self, element, text):
        element.clear()
        element.send_keys(text)

    def get_toast_func(self, text):
        """获取toast信息方法"""
        # 处理传入进来的定位信息
        # xpath = '//*[contains(@text, "再次点击")]' # 文本值不能写死
        xpath = By.XPATH, '//*[contains(@text, "{}")]'.format(text)
        element = self.find_element_func(xpath)  # 调用当前类中的元素定位方法
        return element.text  # 返回目标元素的text属性值

        # element = WebDriverWait(driver, 3, .3). \
        #     until(lambda x: x.find_element_by_xpath('//*[contains(@text, "再次点击")]'))
