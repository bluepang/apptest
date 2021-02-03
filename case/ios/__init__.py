from core.driver import IosDriver
from core.ios_server import IosServer
from common.process_config_file import Config


class BaseCase(object):

    def setup_class(self):
        self.server = IosServer()
        self.app_name = Config().get_target_name()

    def setup_method(self, method):
        self.d = IosDriver.get_driver()
        self.d.home()
        self.d.session().app_activate(self.app_name)

    def teardown_method(self, method):
        self.d.session().app_terminate(self.app_name)

    def teardown_class(self):
        self.server.stop()