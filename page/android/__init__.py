from core.driver import AndroidDriver


class BasePage(object):
    def __init__(self):
        self.d = AndroidDriver.get_driver()

    def open(self, schema):
        self.d.open_url(schema)