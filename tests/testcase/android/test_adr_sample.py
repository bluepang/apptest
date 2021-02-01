from tests.testcase.android.base_case import BaseCase
from tests.pageobjects.android.pick_page import PickPage
from tests.pageobjects.android.edit_page import EditPage
from tests.pageobjects.android.export_done_page import ExportDonePage


class TestSample(BaseCase):

    def test_case01(self):
        PickPage().open()
        PickPage().pick_video_confirm()
        EditPage().direct_export()
        try:
            ExportDonePage().close_pop()
        except:
            pass
        assert ExportDonePage().save_done_label.wait(exists=True, timeout=60)