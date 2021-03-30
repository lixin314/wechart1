from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.base_page import BasePage
from appium_po.page.editmember_page import EditMember


class MoreMenu(BasePage):
    def moremenu(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return EditMember(self.driver)