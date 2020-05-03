import unittest
import HTMLTestRunner
import time
import os

def allTests():
    suite = unittest.defaultTestLoader.discover(
        start_dir=r'D:\Python\UI\testCase',
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

def report():
    fileName = os.path.join(
        r'D:\Python\UI\report',
        getNowTime()+'report.html')
    fp = open(fileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='详细报告')
    runner.run(allTests())
if __name__ == '__main__':
    report()

