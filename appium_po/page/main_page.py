from appium.webdriver.common.mobileby import MobileBy
from appium_po.page.base_page import BasePage
from appium_po.page.contactlist_page import ContactList


class MainPage(BasePage):
    def goto_contact(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactList(self.driver)
