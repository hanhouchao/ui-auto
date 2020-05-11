# -*- coding:utf-8 -*-
from selenium import webdriver
from common.settings import WEB_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 创建基础类
class BasePage(object):
    # 初始化
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://139.186.2.80:37491')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)

    # 定义打开登录页面方法
    def _open(self, url):
        if not url:
            url = WEB_URL
        self.driver.get(url)

    def open(self, url=''):
        self._open(url)

    # 定位方法封装
    def find_element(self, *loc):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc)

    def quit(self):
        self.driver.quit()
