import os
import time
import unittest
import HTMLTestRunner
from framework.browser_engine import BrowserEngine


class Runner(unittest.TestCase):
    # case_path = os.path.dirname(os.path.abspath('.')) + '\\testsuites'
    report_path = os.path.dirname(os.path.abspath('.')) + '/testreport/'
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = report_path + now + "_report.html"
    fp = open(HtmlFile, "wb")
    @classmethod
    def setUpClass(cls):
        print("Start testing")  # 没有输出到控制台
        browser = BrowserEngine()
        browser.open_browser()

    @classmethod
    def tearDownClass(cls):
        print("Stop testing")   # 没有输出到控制台
        browser = BrowserEngine()
        browser.quit_browser()

    def all_case(self):
        # 待执行用例的目录
        case_dir = os.path.join(os.getcwd())
        print(case_dir)
        testcase = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py")
        print(discover)
        # -case_dir:这个是待执行用例的目录。

        # -pattern：这个是匹配脚本名称的规则，test *.py意思是匹配test开头的所有脚本。

        # -top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。

        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_case in discover:
            # 添加用例到 testcase
            testcase.addTests(test_case)
            print(testcase)
        return testcase


# suite1 = unittest.TestLoader().loadTestsFromName(Runner.case_path)
# suite = unittest.TestLoader().discover(Runner.case_path, pattern="test_*.py")


if __name__ == '__main__':
    # unittest.main()
    case = Runner()
    print("000")
    runner = HTMLTestRunner.HTMLTestRunner(stream=Runner.fp, title="测试报告", description="用例情况")
    print("111")
    runner.run(case.all_case())
    print("222")
    Runner.fp.close()
    print("333")
