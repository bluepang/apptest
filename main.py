import pytest
import argparse
from common.process_config_file import set_config
from common.installer import AndroidInstaller, IosInstaller

parse = argparse.ArgumentParser()
parse.add_argument('-p', '--platform', dest='platform', type=str, default='android', help='test platform')
parse.add_argument('-s', '--serial', dest='serial_no', type=str, default='', help='device serinalNo')
parse.add_argument('-n', '--pkg', dest='pkg_name', type=str, default='com.kwai.videoeditor', help='app package name')
parse.add_argument('-u', '--url', dest='app_url', type=str, default='', help='app url')
args = parse.parse_args()

dict = {
    'platform': args.platform,
    'serial_no': args.serial_no,
    'pkg_name': args.pkg_name,
    'app_url': args.app_url
}
set_config(dict)

if __name__ == '__main__':
    if args.platform == 'android':
        case_path = 'testcase/android'
        if args.app_url:
            AndroidInstaller.install()
    else:
        case_path = 'testcase/ios'
        if args.app_url:
            IosInstaller.install()

    pytest.main([case_path])