import subprocess
import time
from common.process_config_file import get_config
from common.logger import Log


class IosServer(object):
    def __init__(self):
        cmd = 'tidevice -u {0} xctest -B {1}'.format(get_config('device_serial'), get_config('wda_app_name'))
        try:
            self.p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        except Exception as e:
            Log().info('ios server start failed: {}'.format(e))
        else:
            Log().info('ios server start successfully')
            time.sleep(5)

    def stop(self):
        self.p.kill()
        Log().info('ios server stop successfully')