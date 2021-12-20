import os

from time import sleep
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpCond
from string import ascii_lowercase, digits


class User():

    def __init__(self, email, pwd):
        if not email:
            self.email = os.environ('BING_EMAIL')
            self.pwd = os.environ('BING_PWD')
        else:
            self.email = email
            self.pwd = pwd


class Browser(Safari):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wait = WebDriverWait(self, 5)

    def send_keys_to_element(self, keys, element, delay=0):
        self.wait.until(ExpCond.presence_of_element_located((By.NAME, element)))
        self.find_element_by_name(element).send_keys(keys + Keys.ENTER)
        sleep(delay)

    def login_to_Microsoft(self, user):
        self.get("https://login.live.com")
        print('Logging you in to your Microsoft account...')
        self.wait.until(ExpCond.url_contains('login.live.com'))

        self.send_keys_to_element(keys=user.email,element='loginfmt',delay=2)
        self.send_keys_to_element(keys=user.pwd,element='passwd',delay=2)
        self.back()
        self.wait.until(ExpCond.title_is('Microsoft account | Home'))
        

    def search_bing(self):
        self.get("https://www.bing.com/")
        sleep(2)

        search_string = digits[:4] + ascii_lowercase
        for char in search_string:
            self.send_keys_to_element(keys=char, element='q', delay=2)
