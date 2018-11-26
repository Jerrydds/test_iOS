import sys, os

import time

sys.path.append(os.getcwd())

from base.base_driver import *
from page.login_page import LoginPage

class TestLogin:

    def setup(self):
        self.driver = init_iOS_driver()
        # self.driver = init_android_driver()
        self.login_page = LoginPage(self.driver)

    def test_login(self):

        # print("111")

        self.login_page.scroll_page_one_time()

        # time.sleep(1)
        # # 点击地狱反按钮
        # self.login_page.click_rice()

