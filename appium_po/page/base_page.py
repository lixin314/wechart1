import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        return self.find(locator, value).click()

    def find_and_sendkeys(self, locator, value, context):
        return self.find(locator, value).send_keys(context)

    def swipe_find(self, num , text ):
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
