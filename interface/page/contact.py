# encoding: utf-8
"""
@author: hei
@file: contact.py
@Date: 2021/3/31
@desc: 
"""
from interface.page.base import Base


class Contact(Base):
    def add_contact(self, userid: str, name: str, mobile: str, department: list):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        result = self.send('POST', url=url, json=data, verify=False)
        return result.json()

    def get_contact(self, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {'userid': userid}
        result = self.send('GET', url=url, params=params, verify=False)
        return result.json()

    def update_contact(self, userid, name):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
        }
        result = self.send('POST',url=url, json=data, verify=False)
        return result.json()

    def delete_contact(self, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {"userid": userid}
        result = self.send('GET', url=url, params=params, verify=False)
        return result.json()