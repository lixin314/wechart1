from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:21503"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_Contact(self):

        '''
        前提条件: 已登录状态（ noReset=True）
        添加通讯录用例：
        1、打开【企业微信】应用
        2、进入【首页】
        3、点击【通讯录】
        4、点击【搜索】
        5、搜索hogwarts_7
        6、点击【hogwarts_7】，进入个人信息
        7、点击【更多】，进入更多菜单页
        8、点击【编辑成员】，进入编辑成员页
        9、点击【删除成员】
        10、判断删除是否成功
        :return:
        '''

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_elements(MobileBy.XPATH,
                                  "//*[@text='我的客户']/../../..//*[@class='android.widget.TextView']")[1].click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys('999')
        sleep(1)
        element = self.driver.find_elements(MobileBy.XPATH, '//*[@text="999"]')
        if len(element) > 1:
            element[-1].click()
        else:
            raise NoSuchElementException(f"cannot found 999 on the search list")
        #print(len(element))
        self.driver.find_element(MobileBy.XPATH,
                                              "//*[@text='个人信息']/../../../../..//*[@class='android.widget.RelativeLayout']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

    def del_verify(self):
        aa = self.driver.find_elements(MobileBy.XPATH, '//*[@text="999"]')
        if len(aa) == 1:
            print('删除成功')


if __name__ == '__main__':
    pytest.main()
