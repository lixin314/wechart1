from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.addcontactlist_page import AddContactList
from appium_po.page.base_page import BasePage
from appium_po.page.searchlist_page import SearchList


class ContactList(BasePage):
    def goto_addcontact_menu(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddContactList(self.driver)

    def goto_searchlist(self):
        self.finds(MobileBy.XPATH,
                                  "//*[@text='我的客户']/../../..//*[@class='android.widget.TextView']")[1].click()
        return SearchList(self.driver)


