import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global driver,username,password
    driver=webdriver.Chrome(ChromeDriverManager().install())
    username=input("enter username")
    password=input("enter password")
    print("Test case Started")
    driver.maximize_window()
    yield
    time.sleep(1)
    driver.close()

def test_login(setUp):
    driver.get("https://www.facebook.com/")
    time.sleep(1)
    driver.find_element_by_id("email").send_keys(username)
    time.sleep(1)
    driver.find_element_by_id("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("login").click()





















