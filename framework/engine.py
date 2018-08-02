#_author:  "小太阳"
#date:  2018/3/28
import os.path
from  configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger = 'BrowserEngine').getlog()

class BrowserEngine(object):
    #编辑驱动目录
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)


        browser = config.get("browserType", "browserName")
        logger.info("你选择的浏览器是： %s." % browser)
        url = config.get("testServer", "URL")
        logger.info("测试网址是: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("开始启动Chrome.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("打开的网址是: %s" % url)

        driver.maximize_window()
        logger.info("最大化当前窗口.")

        driver.implicitly_wait(10)
        logger.info("设置隐式等待10s.")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器.")
        self.driver.quit()