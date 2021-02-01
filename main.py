import pytest
import argparse
from common.process_config_file import set_config
from common.installer import AndroidInstaller, IosInstaller

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform', dest='device_platform', type=str, default='', help='device platform')
parser.add_argument('-s', '--serial', dest='device_serial', type=str, default='', help='device serial no')
parser.add_argument('-n', '--name', dest='app_name', type=str, default='', help='app name')
parser.add_argument('-u', '--url', dest='app_url', type=str, default='', help='app url')

args = parser.parse_args()
conf_dict = {
    'device_platform': args.device_platform,
    'device_serial': args.device_serial,
    'app_name': args.app_name,
    'app_url': args.app_url
}
set_config(conf_dict)


if __name__ == '__main__':
    if args.device_platform == 'android':
        case_path = 'tests/testcase/android'
        if args.app_url:
            AndroidInstaller.install()
    else:
        case_path = 'tests/testcase/ios'
        if args.app_url:
            IosInstaller.install()

    pytest.main([case_path])