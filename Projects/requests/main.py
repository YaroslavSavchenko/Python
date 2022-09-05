from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://yandex.by/")
region = driver.find_element(by=By.CSS_SELECTOR, value='.col headline__item headline__leftcorner>a[data-statlog="head.region.setup"]')
region.click()
pass