from app_tests.testcase.android.base_case import BaseCase
from app_tests.pageobjects.android.home_page import HomePage
from app_tests.pageobjects.android.pick_page import PickPage
from app_tests.pageobjects.android.edit_page import EditPage
from app_tests.pageobjects.android.export_done_page import ExportDonePage


class TestSample(BaseCase):

    def test_case01(self):
        HomePage().open()
        HomePage().goin_pick_page()
        PickPage().pick_video_confirm()
        EditPage().direct_export()
        assert ExportDonePage().save_done_label.wait(exists=True, timeout=60)