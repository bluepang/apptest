from page.android.base_page import BasePage


class EditPage(BasePage):

    def __init__(self):
        super().__init__()
        self.close_button = self.d(resourceId='com.kwai.videoeditor:id/pt')
        self.export_button = self.d(resourceId='com.kwai.videoeditor:id/a70')
        self.edit_tab = self.d(text='剪辑')
        self.direct_export_button = self.d(text='直接导出')

    def direct_export(self):
        self.edit_tab.click()
        self.export_button.click()
        self.direct_export_button.click()

