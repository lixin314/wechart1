from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.addcontact import AddContact
from appium_po.page.base_page import BasePage


class AddContactList(BasePage):
    def goto_addcontact(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return AddContact(self.driver)


