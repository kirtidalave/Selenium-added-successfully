import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
user_input = input("please Enter your user name\n")
user_input2 = input("please Enter your password\n")


driver=webdriver.Chrome(ChromeDriverManager().install())

print("Test case Started")
driver.maximize_window()
driver.get("https://www.instagram.com")
time.sleep(60)
driver.find_elements_by_name("username").send_keys("user_input")
driver.sleep(1)
driver.find_element_by_id("pass").send_keys("user_input2")
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
print("Instagram login done successfully")
print("Test case has successfully completed")