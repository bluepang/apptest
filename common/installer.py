from core.get_driver import AndroidDriver
from common.process_config_file import get_config
from tests.func.init_app import InitApp
import subprocess


class AndroidInstaller(object):
    @staticmethod
    def install():
        driver = AndroidDriver().get_driver()
        # 卸载app
        try:
            driver.app_uninstall(get_config('app_name'))
        except:
            pass
        # 拉起安装程序
        try:
            driver.app_install(get_config('app_url'))
        except:
            pass
        # 根据机型实现不同安装过程
        brand = driver.device_info.get('brand')
        if brand == 'HUAWEI':
            driver(text='继续安装').click()
            driver(text='继续安装').click()
            driver(text='完成').click()
        # 初始化app
        InitApp().init_android_app()


class IosInstaller(object):
    @staticmethod
    def install():
        pass