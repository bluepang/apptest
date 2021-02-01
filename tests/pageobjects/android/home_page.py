from tests.pageobjects import BasePage


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.box_button = self.d(resourceId='com.kwai.videoeditor:id/a1l')
        self.edit_button = self.d(text='剪辑')
        self.shot_button = self.d(text='拍摄')
        self.home_tab - self.d(text='创作')
        self.template_tab = self.d(text='模板')
        self.hot_tab = self.d(text='上热门')
        self.selfcenter_tab = self.d(text='我的')

    def open(self):
        super().open('kwaiying://main')

    def goin_box_page(self):
        self.box_button.click()

    def goin_pick_page(self):
        self.edit_button.click()

    def goin_shot_page(self):
        self.shot_button.click()

    def switch_to_home(self):
        self.hot_tab.click()

    def swith_to_template(self):
        self.template_tab.click()

    def switch_to_hot(self):
        self.hot_tab.click()

    def switch_to_selfcenter(self):
        self.selfcenter_tab.click()

