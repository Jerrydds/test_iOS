import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction


class LoginPage(BaseAction):

    rice_button = By.XPATH, "//*[@name='地狱饭']"

    def click_rice(self):
        self.click(self.rice_button)

