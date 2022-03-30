import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)
driver.close()
print("Test case has successfully completed")

