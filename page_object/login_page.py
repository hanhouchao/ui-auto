from page_object.page_base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_loc = (By.ID, "u")
    password_loc = (By.ID, "p")
    login_loc = (By.ID, "login_button")

    # 输入用户名
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码
    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录
    def type_login(self):
        self.find_element(*self.login_loc).click()


a =  123
a.is_instance()