import pytest
import argparse
from common.process_config_file import set_config

parse = argparse.ArgumentParser()
parse.add_argument('-p', '--platform', dest='platform', type=str, default='android', help='test platform')
parse.add_argument('-s', '--serial', dest='serial_no', type=str, default='', help='device serinalNo')
parse.add_argument('-n', '--pkg', dest='pkg_name', type=str, default='', help='app package name')
args = parse.parse_args()

if __name__ == '__main__':
    dict = {
        'platform': args.platform,
        'serial_no': args.serial_no,
        'pkg_name': args.pkg_name
    }
    set_config(dict)

    if args.platform == 'android':
        case_path = 'app_tests/testcase/android'
    elif args.platform == 'ios':
        case_path = 'app_tests/testcase/ios'
    elif args.platform == 'web':
        case_path = 'web_tests/testcase'
    elif args.platform == 'api':
        case_path = 'api_tests/testcase'

    pytest.main(['-s', case_path])
