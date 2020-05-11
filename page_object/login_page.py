from page_object.page_base import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(BasePage):
    admin_loc = (By.CSS_SELECTOR, "div .dex-subtle-text")
    # org_loc = (By.XPATH, '//input[@name="organization"]')
    username_loc = (By.NAME, "login")
    # username_loc = (By.XPATH, '//input[@id="login"]')
    password_loc = (By.ID, "password")
    login_loc = (By.XPATH, '//button/descendant-or-self::*[normalize-space(text())="登录"]')
    login_title_loc = (By.CSS_SELECTOR, ".account-menu__display")

    # 管理员登陆
    def type_admin(self):
        self.find_element(*self.admin_loc).click()

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

    def login_success(self, timeout=5):
        if self.find_element(*self.login_title_loc).is_displayed():
            return True
        sleep(5)
        timeout -= 1
        self.login_success(timeout=timeout)
