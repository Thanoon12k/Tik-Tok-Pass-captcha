from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://tictok/signup')

# Find the mobile number field and fill it in
mobile_field = browser.find_element(by=By.NAME,value='mobile')
mobile_field.send_keys('xxxxxxxxxx')
browser.quit()