import json
import requests
import pytest


def setup_module(module):
    print('--- setup for module ---')


class LaGou:

    @classmethod
    def setup_class(cls):
        print('--- setup for class')

    def setup_method(self, method):
        self.s = requests.Session()
        self.url = 'https://www.lagou.com'

    @pytest.mark.smoke
    def test_visit_lagou(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        assert '拉勾' in result.text

    # @pytest.mark.skip(reason='没用的跳过')
    def test_get_new_msg(self):
        msg_url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
        cookie = {
            'cookie': '_gid=GA1.2.438589688.1601450871; '
                      'gate_login_token=475844a837230240e1e73e4ecfa34102e65fa8e5384801cca67bbe983a142abb; '
        }
        headers = {'x-l-req-header': 'deviceType: 9}'}
        result = self.s.get(msg_url, cookies=cookie, headers=headers)
        assert result.status_code == 200
        assert json.loads(result.content)['message'] == '成功'

    def teardown_method(self, method):
        self.s.close()

    @classmethod
    def teardown_class(cls):
        print('--- teardown for class ---')


def teardown_module(module):
    print('--- teardown for module ---')