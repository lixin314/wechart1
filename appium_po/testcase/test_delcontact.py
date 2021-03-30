from appium_po.page.app import APP


class Test_DelContact:
    def setup(self):
        self.app = APP().start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    def test_delcontact(self):
        name = '1001'
        delmember = self.main.goto_contact().goto_searchlist().searchlist(name).persion().moremenu()
        delmember.edit_member()
        delmember.del_verify(name)
