from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class formFillOut():
    def __init__(self, email,password):
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.email = email
        self.password = password
    def signIn(self):
        self.browser.get("https://accounts.google.com/")
        emailInput = self.browser.find_elements_by_css_selector("form input")[0]
        emailInput.send_keys(self.email)
        emailInput.send_keys(Keys.ENTER)
        time.sleep(.75)
        passwordInput = self.browser.find_elements_by_css_selector("input[type='password']")[0]
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        
        
    def __exit__(self,exc_type, exc_value, traceback):
        self.browser.close()

x = formFillOut(""" enter your email in this field: """, """ enter your password in this field: """)
x.signIn()
