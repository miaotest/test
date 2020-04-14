"""
统一入口类
"""

from page.index_page import IndexPage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):
    def __init__(self, driver):
        self.driver = driver

    def index_page(self):
        return IndexPage(self.driver)

    def mine_page(self):
        return MinePage(self.driver)

    def login_page(self):
        return LoginPage(self.driver)
