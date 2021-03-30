import yaml
from appium.webdriver.common.mobileby import MobileBy
from ui_framework.page.base_page import BasePage
from ui_framework.page.search_page import Search


class Market(BasePage):
    def goto_search(self):
        self.parse("../page/market.yml", "goto_search")
        return Search(self.driver)
