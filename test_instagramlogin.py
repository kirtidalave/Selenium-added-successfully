import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.instagram.com")
time.sleep(60)
driver.find_elements_by_name("username").send_keys("kirti_____20")
driver.sleep(5)
driver.find_element_by_id("pass").send_keys("Shivanid@123")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(2)
print("Instagram login done successfully")
print("Test case has successfully completed")