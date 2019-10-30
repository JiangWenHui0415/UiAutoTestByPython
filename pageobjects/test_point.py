import time
from framework.browser_engine import BrowserEngine
import unittest


class Point(unittest.TestCase):
    # browser = BrowserEngine()
    # driver = browser.open_browser()
    # @unittest.skip("强制跳过")

    def test_express_point(self):
        """
        点击观点，发表观点
        :return:
        """
        print("click point")
        self.driver.find_element_by_link_text("观点").click()
        print("click input button")
        #driver.find_element_by_xpath("//*[@href='/schemonitor/information-index.html']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name('ke-edit').click()
        self.driver.find_element_by_class_name('ke-edit-iframe').send_keys("UIautoTest")
        # driver.find_element_by_name("")
        self.driver.find_element_by_id("shortFilePublish").click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
