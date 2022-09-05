import time
import re
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

# Поиск пункта "Маркет" и его нажатие
market_link = driver.find_element(by=By.LINK_TEXT, value="Маркет").click()

tabs = driver.window_handles # Получение количества открытых вкладок

select_tab_market = driver.switch_to.window(tabs[1]) # Переключение на другую вкладку

# Получение поля поиска и ввод в него данных
search_input = driver.find_element(by=By.ID, value="header-search")
search_input.send_keys("Note 8")

# Поиск кнопки выполнения поиска и нажатие по ней
search_button = driver.find_element(by=By.CSS_SELECTOR, value="div._3sZwu button[type='submit']").click()

# Ожидание пока не появится элемент на странице
wait = WebDriverWait(driver,60)
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))

# Скролл до указанного елемента, чтоб была видимость 2-х вариантов из найденных результатов поиска
actions = ActionChains(driver)
actions.scroll_to_element(driver.find_element(by=By.CSS_SELECTOR, value="div[data-index='2'] div._1FODI")).perform()

# Получение двух вариантов из поисковых данных и добавление их в сравнение
product_1 = driver.find_element(by=By.CSS_SELECTOR, value="div[data-index='0'] div._1FODI")
product_1.click()
time.sleep(2)
product_2 = driver.find_element(by=By.CSS_SELECTOR, value="div[data-index='1'] div._1FODI")
product_2.click()

# Получение имён выбрнных двух вариантов на странице с результатами поиска
product_1_name = driver.find_element(by=By.CSS_SELECTOR, value="div[data-index='0'] h3>a")
product_2_name = driver.find_element(by=By.CSS_SELECTOR, value="div[data-index='1'] h3>a")

# Создание строки в которой имена двух вариантов взятых для сравнения
products = product_1_name.text + ", " + product_2_name.text

time.sleep(1)
compare_button = driver.find_element(by=By.LINK_TEXT, value="Сравнить").click() # Поиск и нажатие кнопки сравнения

time.sleep(2)
# Получение имён вариантов которые находятся на странице сравнения
compare_phones = driver.find_elements(by=By.CLASS_NAME, value="zvRJM")
# Проверка совпадают ли имена вариантов взятых на странице сравнения и имена вариантов на странице с результатами поиска
for i in compare_phones:
    result = re.search(i.text,products)
    if result:
        print(result[0],"- елемент в сравнении")
    else:
        print("Не совпало")

# Удаление элементов из сравнения
delete_compare = driver.find_element(by=By.XPATH,value='/html/body/div[3]/div[4]/div[2]/div/div[1]/div/div/button').click()

# Ожидание появления кнопки "Войти", чтоб потом выполнить проверку по наличию текста на странице
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cia-vs a.zsSJk._2sWJL._16jAB._36y1j")))
# Проверка, что элементы удалились из сравнения
assert "Сравнивать пока нечего" in driver.page_source
print("Cравнение пусто")

pass