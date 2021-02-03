import pytest
import argparse
import os
from common.process_config_file import Config
from common.installer import Installer

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform', dest='device_platform', type=str, default='', help='device platform')
parser.add_argument('-s', '--serial', dest='device_serial', type=str, default='', help='device serial no')
parser.add_argument('-n', '--name', dest='app_name', type=str, default='', help='app name')
parser.add_argument('-u', '--url', dest='app_url', type=str, default='', help='app url')

args = parser.parse_args()
conf_dict = {
    'device_platform': args.device_platform,
    'device_serial': args.device_serial,
    'target_app_name': args.app_name,
    'target_app_url': args.app_url
}
Config().set_config(conf_dict)


if __name__ == '__main__':
    Installer().install()
    pytest.main(['-s', '-v', os.path.join('case', Config().get_platform()), '--alluredir=./allure_results'])