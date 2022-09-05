import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://yandex.by/")
driver.maximize_window()

check_list = ["Видео", "Картинки", "Новости", "Карты", "Маркет", "Переводчик", "Музыка"]

items = driver.find_elements(by=By.CSS_SELECTOR, value="ul.services-new__list>li")

for i in items:
    select = i.find_element(by=By.TAG_NAME,value="a")
    if select.text in check_list:
       select.click()
       #time.sleep(1)

tab_handle = driver.window_handles
current_handle = driver.current_window_handle

number_tab_handle = len(tab_handle)
tab = number_tab_handle - 1

for i in tab_handle:
    #print(i,"=",tab)
    for j in check_list:
        if j in driver.title:
            print(j,"- "+"link opend")
        elif j.lower() in driver.title:
            print(j, "- " + "link opend")
    driver.switch_to.window(driver.window_handles[tab])
    tab -= 1


pass