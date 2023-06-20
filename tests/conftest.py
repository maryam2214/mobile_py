from sys import path
from os.path import dirname, realpath
#from urllib import request

#from Tools.scripts.win_add2path import PATH
#from exceptiongroup import catch
from pytest import fixture
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import DesiredCapabilities


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------


@fixture(scope="session", autouse=True)
def src():
    """
    Add local src directory to path
    """
    src_path = '{}'.format(dirname(realpath(__file__))[:-5])

    path.insert(0, src_path)


# --------------------------------------------------------------------------------

@fixture
def config(src):
    from support.config_reader import ConfigReader
    config = ConfigReader()
    yield config
    config = None


# --------------------------------------------------------------------------------

@fixture
def driver(config):
    app_path = '{}app\\Android-NativeDemoApp-0.4.0.apk'.format(dirname(realpath(__file__))[:-5])

    caps = {
            'platformName': 'Android', 'automationName': 'uiautomator2', 'deviceName': 'emulator-5554',
            'appPackage': 'com.wdiodemoapp', 'appActivity': '.MainActivity', 'language': 'en', 'locale': 'US',
            'platformVersion': '12.0', 'app': app_path
            }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    yield driver


# --------------------------------------------------------------------------------

@fixture
def login_page(driver):
    from pages.actions.login_page_actions import LoginPageActions

    login_page = LoginPageActions(driver)
    yield login_page
    login_page = None

# --------------------------------------------------------------------------------
