from page.ios import BasePage


class PickPage(BasePage):

    def __init__(self):
        super().__init__()
        self.video_cell_list = self.d(className='XCUIElementTypeCell')
        self.bigscreen_choose_button = self.d(name='album_icon_pic_check_m_normal')
        self.confirm_button = self.d(name='完成')

    def open(self):
        super().open('kwaiying://pick')

    def pick_video_confirm(self, index=0):
        self.video_cell_list[index].click()
        self.bigscreen_choose_button.click()
        self.confirm_button.click()

