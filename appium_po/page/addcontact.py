from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.base_page import BasePage


class AddContact(BasePage):
    def addcontact(self, name, number):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/au0']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eq7']").send_keys(
            number)
        self.find(MobileBy.XPATH, "//*[@text='设置部门']").click()
        self.find(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

    def verifyOk(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
