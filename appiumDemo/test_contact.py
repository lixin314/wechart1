from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


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
        4、点击【添加成员】
        5、点击【手动输入添加】
        6、输入姓名、手机号，设置部门，点击【保存】
        7、判断添加成功
        :return:
        '''

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/au0']").send_keys("777")
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eq7']").send_keys("13800138007")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")


if __name__ == '__main__':
    pytest.main()
