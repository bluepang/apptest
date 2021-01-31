import logging


class Logger(object):
    @staticmethod
    def info(text):
        logging.getLogger().info(text)