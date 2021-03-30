from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


class TestContact:
    def setup(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:21503"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
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

        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='行情']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('alibaba')
        self.driver.find_elements(MobileBy.XPATH, "//*[@text='阿里巴巴']")[0].click()
        sleep(5)



if __name__ == '__main__':
    pytest.main()
