import uiautomator2 as u2
import wda
from common.process_config_file import Config


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
        driver = u2.connect(Config().get_serial())
        return super().get_driver(driver)


class IosDriver(Driver):
    @classmethod
    def get_driver(cls):
        driver = wda.USBClient(Config().get_serial(), port=8100)
        return super().get_driver(driver)