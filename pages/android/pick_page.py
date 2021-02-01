from pages.android.base_page import BasePage


class PickPage(BasePage):
    
    def __init__(self):
        super().__init__()
        self.close_button = self.d(resourceId='com.kwai.videoeditor:id/a1l')
        self.pick_icon_list = self.d(resourceId='com.kwai.videoeditor:id/yz')
        self.confirm_button = self.d(resourceId='com.kwai.videoeditor:id/ac3')

    def open(self):
        super().open('kwaiying://pick')

    def pick_video_confirm(self, index=0):
        self.pick_icon_list[index].click()
        self.confirm_button.click()

