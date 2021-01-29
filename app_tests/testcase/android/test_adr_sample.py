import uiautomator2 as u2
import logging


class TestSample(object):

    def test_case01(self):
        d = u2.connect('UMXDU20A10018714')
        logging.getLogger().info(d.info)