from core.driver import AndroidDriver
from common.process_config_file import Config
from func.init_android_app import init_android_app
from common.download_file import download
from common.logger import Log
import subprocess


class Installer(object):
    def __init__(self):
        self.app_name = Config().get_target_name()
        self.app_url = Config().get_target_url()
        self.serial = Config().get_serial()
        self.platform = Config().get_platform()

    def install(self):
        if self.platform == 'android':
            self.__install_apk()
        else:
            self.__install_ipa()

    def __install_ipa(self):
        try:
            cmd = 'tidevice  -u {0} install {1}'.format(self.serial, self.app_url)
            Log().info(cmd)
            print(cmd)
            p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            p.wait(180)
        except TimeoutError as e:
            Log().info('install ipa timeout')
            raise TimeoutError(self.app_url, 180)
        Log().info('{} installed successfully'.format(self.app_url))

    def __install_apk(self):
        driver = AndroidDriver.get_driver()
        # 卸载app
        try:
            driver.app_uninstall(self.app_name)
        except:
            pass
        # 下载apk并拉起安装程序
        target = "/data/local/tmp/_tmp.apk"
        file_obj = download(self.app_url)
        driver.push(file_obj, target)
        cmd = 'adb -s {0} shell pm install -r -t {1}'.format(self.serial, target)
        Log().info(cmd)
        subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        # 根据机型实现不同安装过程
        brand = driver.device_info.get('brand')
        if brand == 'HUAWEI':
            driver(text='继续安装').click()
            driver(text='继续安装').click()
            driver(text='完成').click()
        # 初始化app
        init_android_app(driver)