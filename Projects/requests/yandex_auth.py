from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://yandex.by/")
login_button = driver.find_element(by=By.LINK_TEXT, value="Войти") # Поиск кнопки "Войти"
login_button.click()

user_name = "yar.savchenko95" # Логин
user_password = "Qwerty+11" # Пароль
input_login_name = driver.find_element(by=By.ID, value="passp-field-login") # Поиск поля имени
input_login_name.send_keys(user_name) # Ввод имени в поле

# Определение функции с действием нажатия кнопки "Войти" на форме логина
def sign_in():
    sign_in_button = driver.find_element(by=By.ID, value="passp:sign-in")
    sign_in_button.click()
sign_in()

wait = WebDriverWait(driver,60)
wait.until(EC.visibility_of_element_located((By.ID,"passp-field-passwd"))) # Ожидание появления кнопки "Войти" после нажатия


input_login_password = driver.find_element(by=By.ID, value="passp-field-passwd") # Поиск поля для ввода пароля
input_login_password.send_keys(user_password) # Ввод пароля в поле
sign_in() # Вызов функции нажатия кнопки "Войти"

assert user_name in driver.page_source # Проверка, присутствует ли имя логина пользователя на странице
print("Пользователь является: ",user_name)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span.avatar__image"))) # Ожидание появления элемента на странице
open_user_list = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="ar.savchenko95") # Поиск всплывающего блока с кнопкой "Выйти"
open_user_list.click() # Открытия всплывающего блока с кнопкой "Выйти"

wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Выйти"))) # Ожидание появления кнопки "Выйти"
logout_button = driver.find_element(by=By.LINK_TEXT, value="Выйти") # Определение кнопки "Выйти"
logout_button.click() # Нажатие на кнопку "Выйти"

assert "Войти" in driver.page_source # Проверка, присутствует ли имя логина пользователя на странице
print("Пользователь: ",user_name,"-", "не авторизован")
pass