from appium.webdriver.common.mobileby import MobileBy

from appium_po.page.base_page import BasePage
from appium_po.page.moremenu_page import MoreMenu


class Persion(BasePage):
    def persion(self):
        self.find(MobileBy.XPATH,
                                 "//*[@text='个人信息']/../../../../..//*[@class='android.widget.RelativeLayout']").click()
        return MoreMenu(self.driver)


