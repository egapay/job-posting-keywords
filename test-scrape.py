import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "./chromedriver.exe"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("https://egapay.github.io/")

search = driver.find_element(By.XPATH, "//div[@id='buttons']//button[text()='Skills']")
print(search.text)
time.sleep(2)
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()