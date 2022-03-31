import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
username=input("enter username")
password=input("enter password")
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(60)
driver.find_element_by_name("username").send_keys(username)
time.sleep(1)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_elements_by_class_name("_8-yf5")
time.sleep(20)
print("test case has successfully completed")