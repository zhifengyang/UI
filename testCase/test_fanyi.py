import unittest
from page.fanyi import *
from page.init import Init
import time
from ddt import data, unpack, ddt
from untils.readExcel import readExcels
from log.user_log import UserLog

log = UserLog()
logger = log.get_log()

@ddt
class fanyiTest(Init, Fanyi):

    @data(*readExcels())
    @unpack
    def test_fanyiLogin_001(self, username, password, result):
        self.login(username, password)
        time.sleep(1)
        logger.info('handle: %s %s %s', username, password, result)
        # logger.error('handle: %s %s %s', username, password, result)
        self.assertEqual(self.getLoginError, result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
