from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://yandex.by/")

login_button = driver.find_element(by=By.LINK_TEXT, value="Войти") # Поиск кнопки "Войти"
login_button.click()

input_login_name = driver.find_element(by=By.ID, value="passp-field-login") # Поиск поля имени
input_login_name.send_keys("NoAutotestUser") # Ввод имени в поле

sign_in_button = driver.find_element(by=By.ID, value="passp:sign-in") # Поиск кнопки "Войти" на форме логина
sign_in_button.click() # Нажатие кнопки "Войти"

wait = WebDriverWait(driver,30)
wait.until(EC.visibility_of_element_located((By.ID,"field:input-login:hint"))) # Ожидание появления сообщения о несуществующем аккаунте

assert "Такого аккаунта нет" in driver.page_source # Проверка, присутствует ли на странице сообщение о несуществующем аккаунте
print("Cообщение о несуществующем аккаунте появляется")

pass