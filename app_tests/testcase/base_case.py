from common.get_driver import AppDriver
from common.process_config_file import get_config


class BaseCase(object):

    def setup_method(self, method):
        self.d = AppDriver().get_driver()
        self.d.screen_on()
        self.d(scrollable=True).scroll.toBeginning()

    def teardown_method(self, method):
        self.d.app_stop(get_config('pkg_name'))
