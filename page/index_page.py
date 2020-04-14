"""
首页
"""
import page
from base.base_page import BasePage


class IndexPage(BasePage):  # 1.根据文件名创建类名
    def click_mine(self):  # 2.将元素的操作与属性组成封装方法
        # 3.使用基类放啊完成元素定位以及操作
        self.click_func(self.find_element_func(page.mine))
