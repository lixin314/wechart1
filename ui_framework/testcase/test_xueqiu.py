from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from ui_framework.page.app import APP


class Test_Xueqiu:
    def setup(self):
        self.app = APP().start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    def test_xueqiu(self):
        self.main.goto_market().goto_search().search()
