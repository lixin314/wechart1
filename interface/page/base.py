# encoding: utf-8
"""
@author: hei
@file: base.py
@Date: 2021/3/31
@desc: 
"""
import requests
import urllib3


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        urllib3.disable_warnings()
        data = {
            "corpid": "1970325009441152",
            "corpsecret": "_7GmbsObsHK6i6i6wxokdiqf1dOa7jMYsaaP4bDVP8s"
        }
        get_token = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=data, verify=False)
        token = get_token.json()['access_token']
        return token

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
