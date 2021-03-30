from appium_po.page.app import APP


class Test_AddContact:
    def setup(self):
        self.app = APP().start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = '1001'
        number = '13800138011'
        addmember = self.main.goto_contact().goto_addcontact_menu().goto_addcontact()
        addmember.addcontact(name, number)
        addmember.verifyOk()
