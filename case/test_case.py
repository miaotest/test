import pytest

from page.page_factory import PageFactory
from utils import get_driver


class TestLogin(object):
    @pytest.fixture()
    def before_func(self): # 相当于setup()
        self.driver = get_driver()
        self.pagefactory = PageFactory(self.driver)  # 实例化统一入口类
        yield
        self.driver.quit()

    def test_func(self):  # 实例化页面操作
        self.pagefactory.index_page().click_mine()
        self.pagefactory.mine_page().click_login()
        self.pagefactory.login_page().login_func('17863272967', 'miao1998')

        username_text = self.pagefactory.mine_page().get_username_text()
        assert '2967' in username_text

    # 错误实例化思路
    # def index_page(self):  # 首页
    #
    #
    # def mine_page(self):  # 我的页面
    #     pass
    #
    # def login_page(self):  # 登录页面
    #     pass
