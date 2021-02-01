from pages.android.base_page import BasePage


class ExportDonePage(BasePage):

    def __init__(self):
        super().__init__()
        self.save_done_label = self.d(text='已保存至相册')
        self.pop_close_btn = self.d(resourceId='com.kwai.videoeditor:id/gs')

    def close_pop(self):
        self.pop_close_btn.click()

