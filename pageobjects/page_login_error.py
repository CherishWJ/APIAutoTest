#_author:  "小太阳"
#date:  2018/4/10
from framework.basepage import BasePage

class Login(BasePage):
    username_input ='id=>user_login'
    password_input = 'id=>user_pass'
    submit_btn = 'id=>wp-submit'
    greeting_link = 'xpath=>//*[@id ="wp-admin-bar-my-account"]/a'
    login_error= "xpath =>//*[@id='login_error']/strong"
    # forget_password ="css=>#nav > a"
    # find = "xpath=>//[@id='wp-submit']"

    def user_name(self,text):
        self.type(self.username_input, text)
    def user_password(self,text):
        self.type(self.password_input, text)
    def send_submit_btn(self):
        self.click(self.submit_btn)
    def get_text_error(self):
        self.text(self.login_error)

