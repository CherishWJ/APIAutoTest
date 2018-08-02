#_author:  "小太阳"
#date:  2018/4/10
from framework.basepage import BasePage

class Remember(BasePage):
    input_box1 = "id=>user_login"
    input_box2 = "id=>user_pass"
    submit_btn = "id=>wp-submit"
    remember_btn="xpath=>//*[@id='rememberme']"

    def user_name(self, text):
        self.type(self.input_box1, text)
    def user_password(self,text):
        self.type(self.input_box2, text)
    def send_submit_btn(self):
        self.click(self.submit_btn)
    def remember_submit_btn(self):
        self.click(self.remember_btn)