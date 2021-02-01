from core.get_driver import AndroidDriver
from common.process_config_file import get_config


class InitApp():
    def __init__(self):
        self.d = AndroidDriver.get_driver()

    def init_android_app(self):
        # 初始化app
        self.d.app_start(get_config('app_name'))
        self.d(text='我知道啦').click()
        self.d(text='始终允许').click()
        self.d(resourceId='com.kwai.videoeditor:id/a7q').click()
        self.d(text='始终允许').click()