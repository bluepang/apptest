from common.get_driver import AppDriver


class BasePage(object):
    def __init__(self):
        self.d = AppDriver.get_driver()

    def open(self, schema):
        self.d.open_url(schema)


