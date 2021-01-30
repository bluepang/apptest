import uiautomator2 as u2
from common.process_config_file import get_config


class AppDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = u2.connect(get_config('serial_no'))
        return cls.driver