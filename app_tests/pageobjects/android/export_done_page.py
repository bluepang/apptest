from app_tests.pageobjects.base_page import BasePage


class ExportDonePage(BasePage):

    def __init__(self):
        super().__init__()
        self.save_done_label = self.d(text='已保存至相册')

    def open(self):
        # super().open('kwaiying://edit')
        pass

