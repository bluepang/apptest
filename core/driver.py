import uiautomator2 as u2
import wda
from common.process_config_file import get_config


class Driver(object):
    driver = None

    @classmethod
    def get_driver(cls, driver):
        if cls.driver is None:
            cls.driver = driver
        return cls.driver


class AndroidDriver(Driver):
    @classmethod
    def get_driver(cls):
        driver = u2.connect(get_config('serial_no'))
        return super().get_driver(driver)


class IosDriver(Driver):
    @classmethod
    def get_driver(cls):
        driver = wda.USBClient(get_config('device_serial'), port=8100)
        return super().get_driver(driver)