from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://yandex.by/")

def city_yet_list(location):

    region = driver.find_element(by=By.CSS_SELECTOR, value='.col>a[data-statlog="head.region.setup"]')
    region.click()  # Нажатие на регион

    city = driver.find_element(by=By.ID, value="city__front-input")
    city.click()
    city.clear()  # Очистка поля оегиона
    city.send_keys(location) # Указание нового региона

    wait = WebDriverWait(driver,10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.popup__content>ul>li")))
    time.sleep(4)
    city.send_keys(Keys.RETURN)

    wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT,"ещё")))
    #time.sleep(5)
    yet = driver.find_element(by=By.LINK_TEXT, value='ещё')
    yet.click() # Нажатие на кнопку "ещё"

    # получение списка содержащего элементы
    list_ul = driver.find_element(by=By.CSS_SELECTOR, value='ul.services-new-more__popup-services')
    items_li = list_ul.find_elements(by=By.TAG_NAME, value='li')  # получение списка элементов

    content = [] # список для хранения полученных названий
    for i in items_li:
        select = i.find_element(by=By.CLASS_NAME, value="services-new__item-title").text
        content.append(select)

    x_button = driver.find_element(by=By.CLASS_NAME, value="services-new-more__popup-close")
    x_button.click() # Закрытие всплывающего блока с элементами

    return content

def conform(one,two):  # Сравнение элементов из двух городов
    if one == two:
        print("Содержимое совпало")
    else:
        print("Содержимое не совпало")

conform(city_yet_list("Париж"),city_yet_list("Лондон"))

#driver.close()

#print(driver.page_source)
#print("Paris = ", city_yet_list("Париж"))
#time.sleep(2)
#print("London = ", city_yet_list("Москва"))

pass