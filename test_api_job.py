import requests
import unittest

url = 'https://mubu.com/login/password'

class TestMubuClass(unittest.TestCase):
    s = requests.session()


    def mubu_login_api(self):
        url = 'https://mubu.com/api/login/submit'
        data = {
            'phone': '15999555574',
            'password': 'qq316118979',
        }
        result = self.s.post(url=url, data=data)
        return result


    def test_create_list(self):
        self.mubu_login_api()
        url = 'https://mubu.com/api/list/create_doc'
        data = {
            'folderId': 0,
            'type': 0
        }
        rep = self.s.post(url=url, data=data)
        assert rep.json()['code'] == 0


