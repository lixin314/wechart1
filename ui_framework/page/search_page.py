from appium.webdriver.common.mobileby import MobileBy
from ui_framework.page.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.parse("../page/search.yml", "search")




