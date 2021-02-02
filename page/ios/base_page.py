from core.driver import IosDriver
from func.open_schema import open_schema


class BasePage(object):
    def __init__(self):
        self.d = IosDriver.get_driver()

    def open(self, schema):
        open_schema(self.d, schema)