from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Указываем что вебдрайвер для браузера Хром + указываем путь
driver = webdriver.Chrome()

#Отображение какой-то страницы
driver.get("http://www.tutorialsninja.com/demo/")

#Поиск елемента
elem_search = driver.find_element(by=By.NAME, value="search")
#Отправить в элемент ввода какие-то нажатия(тоесть текст)
elem_search.send_keys("Iphone")
#Эта команда отправляет специальный символ "RETURN", что эквивалентно нажатию кнопки Энтер
elem_search.send_keys(Keys.RETURN)
# Нахождение элемента по специальныому адресу элемента на странице (xpath)
add_to_card_button = driver.find_element(by=By.XPATH, value="//*[@id=\"content\"]/div[3]/div/div/div[2]/div[2]/button[1]")
add_to_card_button.click()
# Нахождение элемента по содержимому  в теге "title" в теге "<a = href...>"

shop_card_link = driver.find_element(by=By.CSS_SELECTOR, value='.list-inline>li>a[title="Shopping Cart"]')
#shop_card_link = driver.find_element(by=By.TAG_NAME, value="a")
shop_card_link.click()

assert "product 11" in driver.page_source
pass
#driver.close()
