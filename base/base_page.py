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
