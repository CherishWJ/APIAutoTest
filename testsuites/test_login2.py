#_author:  "小太阳"
#date:  2018/4/10
import time
import unittest
from framework.engine import BrowserEngine
from pageobjects.page_login import Login
import csv

class TestLogin(unittest.TestCase):
    '''错误登录测试'''

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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
    # # def test_find_password(self):
    #
    #     login = Login(self.driver)
    #     #login.refresh()
    #     time.sleep(2)
    #     if login.find_element("xpath=>//*[@id='nav']/a").is_displayed:
    #         print(True)
    #     login.link_forget_password()  # 调用页面对象类中的点击忘记密码按钮
    #     time.sleep(5)
    #     login.get_windows_img()  # 调用基类截图方法
    #
    #     try:
    #         self.assertTrue('获取' in login.text(self.find))
    #         print('Test Pass.')
    #     except NameError as e:
    #         print('Test Fail.', format(e))

if __name__ == '__main__':
    unittest.main()
