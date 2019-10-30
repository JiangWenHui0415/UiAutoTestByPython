import time
import unittest
from framework.browser_engine import BrowserEngine


class BaiduSearch(unittest.TestCase):
    browser = BrowserEngine()
    driver = browser.open_browser()

    def test_baidu_search(self):
        """
        以test开头，标识测试用例
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print("Test Pass.")
        except Exception as e:
            print("Test Fail",format(e))

if __name__ == '_main_':
    unittest.main()
