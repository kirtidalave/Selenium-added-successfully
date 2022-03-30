import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.instagram.com")
time.sleep(60)

driver.find_element_by_id("pass").send_keys("")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(2)


print("Test case has successfully completed")