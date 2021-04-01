# encoding: utf-8
"""
@author: hei
@file: test_wechart_contect.py
@Date: 2021/3/31
@desc: 
"""
import pytest

from interface.page.contact import Contact


class Test_WeChart_Contact:

    def setup_class(self):
        self.name = 'hei001'
        self.userid = 'hei001'
        self.number = "+86 17700177000"
        self.department = [1]
        self.contact = Contact()
        #self.new_name = 'lxtest001'

    def setup(self):
        self.contact.delete_contact(self.userid)

    def teardown(self):
        self.contact.delete_contact(self.userid)

    def test_add_contact(self):
        r = self.contact.add_contact(self.userid, self.name, self.number, self.department)
        assert r['errmsg'] == 'created'
        rr = self.contact.get_contact(self.userid)
        assert rr['name'] == self.name

    def test_get_contact(self):
        self.contact.add_contact(self.userid, self.name, self.number, self.department)
        r = self.contact.get_contact(self.userid)
        assert r['name'] == self.name

    @pytest.mark.parametrize("new_name", ["gaga111"]*5)
    def test_update_contact(self, new_name):
        self.contact.add_contact(self.userid, self.name, self.number, self.department)
        r = self.contact.update_contact(self.userid, new_name)
        assert r['errmsg'] == 'updated'
        rr = self.contact.get_contact(self.userid)
        assert rr['name'] == new_name

    def test_del_contact(self):
        self.contact.add_contact(self.userid, self.name, self.number, self.department)
        r = self.contact.delete_contact(self.userid)
        assert r['errmsg'] == 'deleted'
        rr = self.contact.get_contact(self.userid)
        assert rr['errcode'] == 60111
