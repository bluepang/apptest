import requests
import os
import sys
import json
import urllib3
from common.process_config_file import get_config
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class LoginStatus:
    def __init__(self):
        self.host = get_config('host', 'host_production')
        self.s = requests.Session()
        self.login_path = 'project/api/project/auth/login'

    def login(self, username, passwd):
        login_data = {
            'email': username,
            'password': passwd
        }
        res = self.s.post(
            os.path.join(self.host, self.login_path),
            data=json.dumps(login_data),
            verify=False
        )
        print(res.status_code)
        print(res.text)
        return self.s


if __name__ == '__main__':
    LoginStatus().login('772840357@qq.com', 'yang1990315')