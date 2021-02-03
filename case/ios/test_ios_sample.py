from case.ios import BaseCase
from page.ios.pick_page import PickPage
import time


class TestIosSample(BaseCase):
    def test_case01(self):
        PickPage().open()
        time.sleep(10)