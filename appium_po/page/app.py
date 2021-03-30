import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_po.page.base_page import BasePage
from appium_po.page.main_page import MainPage
# 进入通讯录
with open("../data/caps.yml",encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class APP(BasePage):
    def start(self):
        if self.driver == None:
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart_app(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)

