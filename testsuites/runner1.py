import os
import time
import unittest
import HTMLTestRunner
from selenium import webdriver
from framework.browser_engine import BrowserEngine


# class Runner1(unittest.TestCase):
#     browserEngine = BrowserEngine()
#     driver = browserEngine.open_browser()
#
#     @classmethod
#     def setUpClass(cls):
#         print("test start\n")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("test over")
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#     report_path = os.path.dirname(os.path.abspath('.')) + '/testreport/'
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     HtmlFile = report_path + now + "_report.html"
#     fp = open(HtmlFile, "wb")
#     case_dir = os.path.join(os.getcwd())
#     print("dir===" + case_dir)
#     suite = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py')
#     print("case===", suite)
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="用例情况")
#     runner.run(suite)

report_path = os.path.dirname(os.path.abspath('.')) + '/testreport/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = report_path + now + "_report.html"
fp = open(HtmlFile, "wb")
case_dir = os.path.join(os.getcwd())
print("dir===" + case_dir)
suite = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py')
print("case===", suite)
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="用例情况")
runner.run(suite)
