from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())
driver.get("https://www.nseindia.com/")
print(driver.title)
driver.maximize_window()
