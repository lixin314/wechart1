import yaml
from appium.webdriver.common.mobileby import MobileBy
from ui_framework.page.base_page import BasePage
from ui_framework.page.market_page import Market


class MainPage(BasePage):
    def goto_market(self):
        self.parse("../page/main.yml", "goto_market")
        return Market(self.driver)


