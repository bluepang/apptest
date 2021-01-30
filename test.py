import uiautomator2 as u2
from app_tests.pageobjects.android.edit_page import EditPage
from app_tests.pageobjects.android.pick_page import PickPage

# d = u2.connect()

PickPage().open()
PickPage().pick_video_confirm()
EditPage().direct_export()