import requests
import urllib3


def get_token():
    urllib3.disable_warnings()
    get_token = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=1970325009441152&corpsecret=_7GmbsObsHK6i6i6wxokdiqf1dOa7jMYsaaP4bDVP8s',verify=False)
    token = get_token.json()['access_token']
    return token


def test_add_contact():
    urllib3.disable_warnings()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "lxtest",
        "name": "lxtest1",
        "mobile": "+86 18800188000",
        "department": [1],
     }
    result = requests.post(url=url, json=data, verify=False)
    print(result.json())
    assert result.json()['errmsg'] == 'created'


def test_get_contact():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=lxtest'
    result = requests.get(url=url, verify=False)
    print(result.json())
    assert result.json()['name'] == 'lxtest1'


def test_update_contact():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data ={
        "userid": "lxtest",
        "name": "lxtest2",

    }
    result = requests.post(url=url, json=data, verify=False)
    print(result.json())
    assert result.json()['errmsg'] == 'updated'


def test_delete_contact():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=lxtest'
    result = requests.get(url=url, verify=False)
    print(result.json())
    assert result.json()['errmsg'] == 'deleted'