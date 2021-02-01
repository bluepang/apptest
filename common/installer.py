from core.driver import AndroidDriver
from common.process_config_file import get_config
from func.init_app import InitApp
from common.download_file import download
from common.logger import Log
import subprocess


class AndroidInstaller(object):
    @staticmethod
    def install():
        driver = AndroidDriver.get_driver()
        # 卸载app
        try:
            driver.app_uninstall(get_config('app_name'))
        except:
            pass

        # 下载apk并拉起安装程序
        target = "/data/local/tmp/_tmp.apk"
        file_obj = download(get_config('app_url'))
        driver.push(file_obj, target)
        Log().info("pm install -rt {}".format(target))
        cmd = 'adb -s {0} shell pm install -r -t {1}'.format(get_config('device_serial'), target)
        Log().info(cmd)
        subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

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