import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://yandex.by/")
driver.maximize_window()
wait = WebDriverWait(driver,60)
actions = ActionChains(driver)
# Поиск пункта "Маркет" и его нажатие
market_link = driver.find_element(by=By.LINK_TEXT, value="Маркет").click()

tabs = driver.window_handles # Получение количества открытых вкладок
switch_tab = driver.switch_to.window(tabs[1]) # Переключение на вкладку "Маркет"

# Поиск пункта "Электроника" и нажатие по нему
electronics_link = driver.find_element(by=By.LINK_TEXT,value="Электроника").click()

# Ожидание пока загрузится страница
wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body")))

# Поиск пункта "Экшн-камеры" и нажатие по нему
action_cameras = driver.find_element(by=By.LINK_TEXT,value="Экшн-камеры").click()

sort_price = driver.find_element(by=By.CSS_SELECTOR, value="div._16jig button[data-autotest-id='dprice']")

link_color_before_click = sort_price.value_of_css_property("color")

actions.double_click(sort_price).perform()

link_color_after_click = driver.find_element(
    by=By.CSS_SELECTOR, value="div._16jig button[data-autotest-id='dprice']"
    ).value_of_css_property("color")

if link_color_after_click == "rgba(255, 0, 0, 1)":
    print("Отсортировано по цене")
elif link_color_before_click == "rgba(0, 68, 187, 1)":
    print("Сортировано по цене НЕ выбрана")
else:
    print("Непредвиденное условие")

pass

