"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    def input_user(self, user):  # 输入用户名
        self.input_func(self.find_element_func(page.user), user)

    def input_pwd(self, pwd):  # 输入密码
        self.input_func(self.find_element_func(page.pwd), pwd)

    def click_login(self):  # 登录点击
        self.click_func(self.find_element_func(page.login_btn))

    def click_confirm(self):  # 登录提示消息确认
        self.click_func(self.find_element_func(page.confirm_btn))

    def login_func(self, user, pwd):
        self.input_user(user)
        self.input_pwd(pwd)
        self.click_login()
        self.click_confirm()