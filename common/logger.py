import logging


class Log(object):
    def __init__(self):
        self.log = logging.getLogger()

    def info(self, text):
        self.log.info(text)
