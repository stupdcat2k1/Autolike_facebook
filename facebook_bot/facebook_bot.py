from random import randint
from time import sleep, time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from webdriver_manager.chrome import ChromeDriverManager


def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))


class facebook_bot():
    def __init__(self, url, username, password):
        option = Options()
        option.add_argument("----disable-notifications")
        option.add_argument("----disable-infobars")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(url)
        self.login(username, password)

    def login(self, username, password):
        email_box = self.driver.find_element_by_id('email')
        email_box.send_keys(username)
        random_sleep(1, 3)
        pass_box = self.driver.find_element_by_id('pass')
        pass_box.send_keys(password)
        random_sleep(1, 3)
        login_btn = self.driver.find_element_by_name('login')
        login_btn.send_keys(Keys.RETURN)
        random_sleep(1, 3)

    def like1(self):
        test = Controller()
        random_sleep(2, 3)
        for i in range(5):
            test.press('j')
            test.release('j')
            random_sleep(1, 2)
            test.press('l')
            test.release('l')
            random_sleep(1, 2)
            test.press(Key.space)
            test.release(Key.space)
            random_sleep(1, 2)
            print("Đã like bài thứ: ", i+1)

    def like2(self):
        self.driver.get("https://www.facebook.com/")
        test = Controller()
        random_sleep(2,3)
        for i in range(5):
            if (i == 0):
                test.press('j')
                test.release('j')
                random_sleep(1, 2)
            test.press('j')
            test.release('j')
            random_sleep(1, 2)
            test.press('l')
            test.release('l')
            random_sleep(1, 2)
            test.press(Key.space)
            test.release(Key.space)
            random_sleep(1, 2)
            print("Đã like bài thứ: ", i+1)

    def likev2(self):
        self.driver.execute_script("window.scrollTo(0, 990);")
        random_sleep(4, 5)
        likes = self.driver.find_elements_by_xpath("//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
        print(len(likes))
        action = ActionChains(self.driver)
        random_sleep(1, 2)
        for i in range(len(likes)):
            action.move_to_element(likes[i]).perform()
            random_sleep(1, 2)
            self.driver.execute_script("arguments[0].click();", likes[i])
            random_sleep(1, 2)
            print("Đã like bài ", i + 1)
            random_sleep(1, 2)
            action.reset_actions()
            random_sleep(2,2)
        print("Đã chạy xong v2")