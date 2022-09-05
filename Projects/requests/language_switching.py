import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://yandex.by/")
driver.maximize_window()

def settings_page(settings):
    actions = ActionChains(driver)
    actions.scroll_by_amount(delta_x=0,delta_y=1200).perform() # Прокрутка страницы чтоб появился пункт "Настройка"
    time.sleep(1)

    setting = driver.find_element(by=By.LINK_TEXT, value="Настройка").click() #Поиск пункта "Настройка" и нажатие по нему
    time.sleep(1)
    settings_portal = driver.find_element(by=By.LINK_TEXT,value="Настройки портала").click() #Поиск пункта "Настройки портала" и нажатие по нему

    general_settings = driver.find_element(by=By.LINK_TEXT,value=settings).click() #Поиск пункта "Общие настройки" и нажатие по нему

settings_page("Общие настройки") # вызов функции перехода в настройки в раздел где менять язык

#Поиск кнопки для выбора языка и нажатие по ней
language_button = driver.find_element(by=By.XPATH, value='//*[@id="form__a11y"]/div[2]/div[2]/div/div[1]/div[1]/button')
language_button.click()

# Получения списка языков
dropdown_language = driver.find_elements(by=By.CSS_SELECTOR, value="div.popup__content div.select__list>div.select__item")

# Перебор списка языков для выбора английского
for i in dropdown_language:
    if i.text == "English":
        english_id = i.get_attribute("id") # Получение id блока с английским языком
        select_english_item = driver.find_element(by=By.ID, value=english_id).click()

save_button = driver.find_element(by=By.CSS_SELECTOR,value="div.form__controls button[type='submit']").click()

time.sleep(2)

settings_page("General settings") # вызов функции перехода в настройки в раздел где менять язык

#Поиск кнопки для выбора языка, чтоб проверить актиыный язык
check_language = driver.find_element(by=By.XPATH, value='//*[@id="form__a11y"]/div[2]/div[2]/div/div[1]/div[1]/button')

if check_language.text == "English":
    print("Установленный язык - ", check_language.text)

pass