from random import randint
from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key,Controller
def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))
class facebook_bot():
    def __init__(self, driver, url, username, password):
        option = Options()
        option.add_argument("----disable-notifications")
        option.add_argument("----disable-infobars")
        self.driver = webdriver.Chrome(driver,chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(url)
        self.login(username, password)

    def login(self, username, password):
        email_box = self.driver.find_element_by_id('email')
        email_box.send_keys(username)
        random_sleep(1, 5)
        pass_box = self.driver.find_element_by_id('pass')
        pass_box.send_keys(password)
        random_sleep(1, 5)
        pass_box.send_keys(Keys.RETURN)
        random_sleep(1,5)

    def like(self):
        i = 0
        random_sleep(5, 7)
        test = Controller()
        while i<=5:
            random_sleep(1, 2)
            test.press('j')
            test.release('j')
            random_sleep(1, 2)
            test.press('l')
            test.release('l')
            random_sleep(1, 2)
            test.press(Key.enter)
            test.release(Key.enter)
            i+=1
        print("Đã like xong")
