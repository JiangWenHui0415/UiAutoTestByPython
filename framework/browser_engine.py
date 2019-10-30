import os.path
from selenium import webdriver
from framework.logger import Logger
from config import config


logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine:
    # 获取当前项目的根目录的相对路径
    dir = os.path.dirname(os.path.abspath('.'))   # 获取相对路径
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/iedriver.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self):
        print("init browser engine")
        self.url = config.URL
        browser = config.browserName
        logger.info("you had select %s browser" % browser)
        logger.info("The test server URL is: %s " % self.url)
        if browser == "Firefox":
            self.driver = webdriver.Firefox()
            logger.info("Starting Firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie
            logger.info("Starting IE browser.")
        else:
            logger.info("browser error,please check the config file")
            exit(code=1)  # 退出该测试流程
        print("selected driver=", self.driver)

    def open_browser(self):
        self.driver.get(self.url)
        logger.info("Open url is: %s " % self.url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return self.driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()


