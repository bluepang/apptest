from core.driver import IosDriver
from core.ios_server import IosServer
from common.process_config_file import get_config


class BaseCase(object):

    def setup_class(self):
        self.server = IosServer()

    def setup_method(self, method):
        self.d = IosDriver.get_driver()
        self.d.home()
        self.s = self.d.session(get_config('app_name'))

    def teardown_method(self, method):
        self.s.app_terminate(get_config('app_name'))

    def teardown_class(self):
        self.server.stop()