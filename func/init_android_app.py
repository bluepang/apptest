from common.process_config_file import Config


def init_android_app(self, driver):
    # 初始化app
    driver.app_start(Config().get_target_name())
    driver(text='我知道啦').click()
    driver(text='始终允许').click()
    driver(resourceId='com.kwai.videoeditor:id/a7q').click()
    driver(text='始终允许').click()