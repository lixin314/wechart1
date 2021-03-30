import allure
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.page.logger import log


def blacklist(fun):
    def run(*args, **kwargs):
        black_list = ["//*[@resource-id='com.xueqiu.android:id/iv_close']"]
        self = args[0]

        try:
            log.debug('find' + args[2])
            return fun(*args, **kwargs)
        except Exception as e:
            allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
            for i in black_list:
                eles = self.finds(MobileBy.XPATH, i)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)

    return run

