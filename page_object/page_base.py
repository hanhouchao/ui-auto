# -*- coding:utf-8 -*-
from common.settings import WEB_URL, TOKEN
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 创建基础类
class BasePage(object):
    driver = None

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 定义打开登录页面方法
    def _open(self, url, token):
        open_url = ""
        # if not url:
        #     url = WEB_URL
        if token:
            open_url = "{}/{}?id_token={}".format(WEB_URL, url, token)
        self.driver.get(open_url)

    def open(self, url='', token=TOKEN):
        self._open(url, token=token)

    # 定位方法封装
    def find_element(self, *loc):
        WebDriverWait(self.driver, 30,
                      0.5).until(EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc)

    # 定位方法封装
    def find_elements(self, *loc):
        WebDriverWait(self.driver, 30,
                      0.5).until(EC.presence_of_element_located(loc))
        return self.driver.find_elements(*loc)

    # 切换标签页
    def switch_window(self, index=0):
        '''
        @param index 窗口的index 从0 开始
        @exp switch_window(1)
        '''
        handle = self.driver.window_handles[index]
        self.driver.switch_to.window(handle)

    # 切换frame内嵌页
    def switch_frame(self, *loc):
        '''
        @param *loc 内嵌页面的元素地址
        @exp switch_frame(1)
        '''
        self.driver.switch_to.frame(*loc)

    def get_element_by_text(self, text, type="button"):
        xpath = "//{type}/descendant-or-self::*[normalize-space(text()) ='{text}']".format(type=type, text=text)
        return self.find_element(*(By.XPATH, xpath))

    def fill_form(self, data, parent_css="rc-image-input .aui-form-item.aui-form-item--right"):
        eles = self.find_elements(*(By.CSS_SELECTOR, parent_css))
        for key, value in data.items():
            for ind, ele in enumerate(eles):
                if ele.text.find(key) >= 0:
                    self.find_element(
                        *(By.CSS_SELECTOR,
                          "{}:nth-of-type({}) input".format(parent_css, ind + 1))).send_keys(value)

    def quit(self):
        self.driver.quit()

    def capture_screenshot(self):
        self.driver.save_screenshot()
        return self.driver.get_screenshot_as_base64()
