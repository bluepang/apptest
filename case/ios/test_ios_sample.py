from case.ios.base_case import BaseCase
from page.ios.pick_page import PickPage
import time


class TestIosSample(BaseCase):
    def test_case01(self):
        PickPage().open()
        PickPage().pick_video_confirm()
        time.sleep(10)