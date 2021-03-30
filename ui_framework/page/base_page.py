import logging

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from ui_framework.page.blacklist import blacklist


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @blacklist
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def finds_and_click(self, locator, value, num):
        return self.driver.find_elements(locator, value)[num].click()

    def find_and_click(self, locator, value):
        return self.find(locator, value).click()

    def find_and_sendkeys(self, locator, value, context):
        return self.find(locator, value).send_keys(context)

    def parse(self, yaml_path, func_name):
        """
        获取yaml文件中的字段
        :param funname: 函数名
        :return:
        """
        with open(yaml_path, 'r', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            steps = datas.get(func_name)
            for step in steps:
                if step['action'] == 'find_and_click':
                    self.find_and_click(step.get('locator'), step.get('value'))
                elif step['action'] == 'find_and_sendkeys':
                    self.find_and_sendkeys(step.get('locator'), step.get('value'), step.get('context'))
                elif step['action'] == 'finds_and_click':
                    self.finds_and_click(step.get('locator'), step.get('value'), step.get('num'))

    def screenshot(self):
        return self.driver.get_screenshot_as_png()

    def swipe_find(self, num, text):
        for i in range(num):
            if i == num - 1:
                logging.info("set implicitly_wait :5")
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")
            logging.info("set implicitly_wait :1")
            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
