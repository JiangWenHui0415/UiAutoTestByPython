# coding=utf-8
import time
import os
from framework.logger import Logger
from selenium import *

#creat a logger instance
logger = Logger(logger="BasePage").getlog()

class BasePage():
    """
    定义一个页面基类，让所有的页面继承该类
    封装一些常用的页面操作方法到这个类
    """
    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info("click forward on current page.")

    def backward(self):
        self.backward()
        logger.info("click backward on current page.")

    def wait(self,seconds):
        self.driver.implicitly.wait(seconds)
        logger.info("wait for %d seconds."  % seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser")
        except NameError as e:
            logger.info("Failed to close the browser with %s" % e)

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.info("Failed to take screenshot! %s" %e)
            self.get_windows_img()

