from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from appium_po.page.base_page import BasePage
from appium_po.page.persion_page import Persion


class SearchList(BasePage):
    def searchlist(self,name):

        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        sleep(1)
        element = self.finds(MobileBy.XPATH, f'//*[@text="{name}"]')
        if len(element) > 1:
            element[-1].click()
            return Persion(self.driver)

        else:
            raise NoSuchElementException(f"cannot found {name} on the search list")

