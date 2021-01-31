from pageobjects.android import EditPage
from pageobjects.android import PickPage

# d = u2.connect()

PickPage().open()
PickPage().pick_video_confirm()
EditPage().direct_export()