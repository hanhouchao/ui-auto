# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#创建基础类
class BasePage(object):
    #初始化
    def __init__(self, driver):
        self.base_url = 'https://mail.qq.com/'
        self.driver = driver
        self.timeout = 30

    #定义打开登录页面方法
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        self.driver.switch_to.frame('login_frame')  #切换到登录窗口的iframe

    def open(self):
        self._open()

    #定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

#创建LoginPage类
class LoginPage(BasePage):
    username_loc = (By.ID, "u")
    password_loc = (By.ID, "p")
    login_loc = (By.ID, "login_button")

    #输入用户名
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #输入密码
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    #点击登录
    def type_login(self):
        self.find_element(*self.login_loc).click()

#创建test_user_login()函数
def test_user_login(driver, username, password):
    """测试用户名/密码是否可以登录"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login()

#创建main()函数
def main():
    driver = webdriver.Chrome()
    username = '954807595'    #qq号码
    password = 'qq19900913!'    #qq密码
    test_user_login(driver, username, password)
    sleep(3)

    driver.quit()

if __name__ == '__main__':
    main()
