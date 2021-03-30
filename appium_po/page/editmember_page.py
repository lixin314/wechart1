from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.base_page import BasePage


class EditMember(BasePage):
    def edit_member(self):
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()

    def del_verify(self, name):
        member = self.finds(MobileBy.XPATH, f'//*[@text="{name}"]')
        if len(member) == 1:
            print('删除成功')


