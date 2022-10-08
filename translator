from gettext import translation
import time
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from speechtotext import gets

drivers = webdriver.Chrome()
drivers.get("https://translate.google.co.in/")
time.sleep(3)
drivers.find_element(By.CLASS_NAME, "er8xn").send_keys(gets)
time.sleep(3)
url = drivers.current_url
time.sleep(3)
translated=drivers.find_element(By.CLASS_NAME, "Q4iAWc")
translated=translated.text
print(translated)