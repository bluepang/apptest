from common.get_driver import AndroidDriver, IosDriver
from common.process_config_file import get_config
from pageobjects.android.home_page import HomePage
from pageobjects.android.pick_page import PickPage
from pageobjects.android.edit_page import EditPage
from pageobjects.android.export_done_page import ExportDonePage
import time


class AndroidInstaller(object):
    @staticmethod
    def install():
        driver = AndroidDriver().get_driver()
        try:
            driver.app_uninstall(get_config('pkg_name'))
        except:
            pass
        try:
            driver.app_install(get_config('app_url'))
        except:
            pass
        try:
            driver(text='继续安装').click()
            driver(text='继续安装').click()
            driver(text='完成').click()
        except:
            pass
        driver.app_start(get_config('pkg_name'))
        HomePage().switch_to_home()
        HomePage().switch_to_home()
        HomePage().goin_pick_page()
        PickPage().pick_video_confirm()
        EditPage().direct_export()
        ExportDonePage().close_pop()
        time.sleep(3)
        driver.app_stop(get_config('pkg_name'))


class IosInstaller(object):
    @staticmethod
    def install():
        pass