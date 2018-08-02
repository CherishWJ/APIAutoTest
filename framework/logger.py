#_author:  "小太阳"
#date:  2018/3/28


import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):
        #创建一个logger接收器
        self.logger = logging.getLogger(logger)
        #设置日志输出等级
        self.logger.setLevel(logging.DEBUG)

        #创建一个hander,处理器，用于写入日志文件

        #提取系统时间
        rq = time.strftime('%Y%m%d%H%M')
        #定义日志位置
        log_path = os.path.dirname(os.getcwd())+'/logs/'
        #定义log名称
        log_name = log_path+rq+'.log'
        #创建一个处理器输出到日志文件
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 创建一个处理器输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

         #定义hander的输出格式
        formatter = logging.Formatter(('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加hander
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
