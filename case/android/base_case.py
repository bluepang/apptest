from core.driver import AndroidDriver
from common.process_config_file import get_config


class BaseCase(object):

    def setup_method(self, method):
        self.d = AndroidDriver.get_driver()
        if not self.d.info.get('screenOn'):
            self.d.screen_on()
            self.d(scrollable=True).scroll.toBeginning()
        self.d.app_start(get_config('app_name'))

    def teardown_method(self, method):
        self.d.app_stop(get_config('app_name'))