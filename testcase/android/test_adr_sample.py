from testcase.android.base_case import BaseCase
from pageobjects.android.pick_page import PickPage
from pageobjects.android.edit_page import EditPage
from pageobjects.android.export_done_page import ExportDonePage


class TestSample(BaseCase):

    def test_case01(self):
        PickPage().open()
        PickPage().pick_video_confirm()
        EditPage().direct_export()
        assert ExportDonePage().save_done_label.wait(exists=True, timeout=60)