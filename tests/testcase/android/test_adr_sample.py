from tests.testcase.android.base_case import BaseCase
from tests.pageobjects import PickPage
from tests.pageobjects import EditPage
from tests.pageobjects import ExportDonePage


class TestSample(BaseCase):

    def test_case01(self):
        PickPage(self.d).open()
        PickPage(self.d).pick_video_confirm()
        EditPage(self.d).direct_export()
        assert ExportDonePage(self.d).save_done_label.wait(exists=True, timeout=60)