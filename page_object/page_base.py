# -*- coding:utf-8 -*-
from selenium import webdriver


# 创建基础类
class BasePage(object):
    # 初始化
    def __init__(self):
        self.base_url = 'https://mail.qq.com/'
        self.driver = webdriver.Chrome()
        self.timeout = 30

    # 定义打开登录页面方法
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        self.driver.switch_to.frame('login_frame')  # 切换到登录窗口的iframe

    def open(self):
        self._open()

    # 定位方法封装
    def find_element(self, *loc):
        print(*loc)
        return self.driver.find_element(*loc)

    def quit(self):
        self.driver.quit()
