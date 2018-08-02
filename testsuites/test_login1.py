#_author:  "小太阳"
#date:  2018/4/2
import time
import unittest
from framework.engine import BrowserEngine
from pageobjects.page_login import Login
import csv

class TestLogin(unittest.TestCase):
    '''登录测试'''
    # file = open('../file/user_info.csv', 'r')
    # date = csv.reader(file)
    # #定义一个用户数组
    # users = []
    # #循环输出每一行
    # for user in date:
    #     users.append(user)
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_login(self):
        '''正确测试'''
        login = Login(self.driver)
        login.user_name('anjing')  # 调用页面对象中的方法
        login.user_password('anjing123456')
        login.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        login.get_windows_img()  # 调用基类截图方法
        login.back()
        try:
            self.assertTrue('anjing' in login.get_text_greeting())
            print(login.get_text_greeting())
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
    def test_login_error(self):
        '''错误测试'''
        login = Login(self.driver)
        login.user_name('anjing')  # 调用页面对象中的方法
        login.user_password('anjing')
        login.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        login.get_windows_img()  # 调用基类截图方法

        try:
            self.assertTrue('错误' in login.get_text_error())
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
if __name__ == '__main__':
    unittest.main()
