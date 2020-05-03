import logging
import os
import datetime

class UserLog(object):
    # 构造函数
    def __init__(self):
        # 获取 logger 对象
        self.logger = logging.getLogger()
        # 定义日志级别
        self.logger.setLevel(logging.DEBUG)
        # 定义日志文件路径（当前文件所在的路径）
        log_dir = os.path.dirname(__file__)
        # 定义日志文件名
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        # 定义日志文件全路径
        log_name = log_dir + '/' + log_file
        # 获取文件处理器
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        # 重定义输出日志级别
        self.file_handle.setLevel(logging.INFO)
        # 定义日志输出格式
        formatter = logging.Formatter('%(asctime)s %(name)s %(filename)s %(funcName)s %(levelname)s --> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

    # def get_sleep_log(self):
    #     log_dir = os.path.join(os.path.dirname(__file__))
    #     # 定义日志文件名
    #     log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
    #     # 定义日志文件全路径
    #     log_name = log_dir + '/' + log_file
    #     # 获取文件处理器
    #     self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
    #     # 重定义输出日志级别
    #     self.file_handle.setLevel(logging.ERROR)
    #     # 定义日志输出格式
    #     formatter = logging.Formatter('%(asctime)s %(name)s %(filename)s %(funcName)s %(levelname)s --> %(message)s')
    #     self.file_handle.setFormatter(formatter)
    #     self.logger.addHandler(self.file_handle)
    #     return self.logger

# if __name__ == '__main__':
#     log = UserLog().get_log()
#     log.debug("t1")
#     UserLog().close_handle()