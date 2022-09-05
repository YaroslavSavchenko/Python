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
wait = WebDriverWait(driver,60)
actions = ActionChains(driver)

LOGIN = "yar.savchenko95"
PASSWORD = "Qwerty+111"
login_button = driver.find_element(by=By.LINK_TEXT, value="Войти").click() # Поиск кнопки "Войти"
input_login_name = driver.find_element(by=By.ID, value="passp-field-login") # Поиск поля имени
time.sleep(1)
input_login_name.send_keys(LOGIN) # Ввод имени в поле

def sign_in():
    sign_in_button = driver.find_element(by=By.ID, value="passp:sign-in")
    sign_in_button.click()

sign_in()

wait.until(EC.visibility_of_element_located((By.ID,"passp-field-passwd"))) # Ожидание появления кнопки "Войти" после нажатия

input_login_password = driver.find_element(by=By.ID, value="passp-field-passwd") # Поиск поля для ввода пароля
input_login_password.send_keys(PASSWORD) # Ввод пароля в поле
sign_in() # Вызов функции нажатия кнопки "Войти"

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.home-logo__default[aria-label='Яндекс']")))

music_link = driver.find_element(by=By.LINK_TEXT, value="Музыка").click()

tabs = driver.window_handles
swithc_tab = driver.switch_to.window(tabs[1])

#wait.until_not(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[16]/div/div/div[2]/div/div[1]/div/div[2]/span")))

#close_subscription_screen = driver.find_element(
#    by=By.XPATH, value='/html/body/div[1]/div[16]/div/div/div[2]/div/div[1]/div/div[2]/span')
#close_subscription_screen.click()

search_button = driver.find_element(by=By.CSS_SELECTOR,value="div.d-search__button__container button[type='submit']").click()

search_input = driver.find_element(
    by=By.CSS_SELECTOR,value="div.d-suggest input[placeholder='Трек, альбом, исполнитель, подкаст']")
search_input.send_keys("Imprint")

time.sleep(3)

list_group = driver.find_elements(by=By.CLASS_NAME, value="d-suggest-item__title")

worship_group = "0"

for i in list_group:
    if i.text == "Imprintband":
        worship_group = i.text
        print(f"- Выбор из списка группы '{worship_group}' выполнен успешно")
        actions.click(i).perform()

#Проверка артиста
wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME,"h2")))
artiste = driver.find_element(by=By.CSS_SELECTOR,value="h1.typo-h1")
if artiste.text == worship_group:
    print(f"- Исполнитель соответствует: '{worship_group}'")
else:
    print(f"- Артист  = '{artiste.text}' - не совпал")

#Проверка в популярных альбомах
popular_albums = driver.find_elements(by=By.CSS_SELECTOR,value="div.page-artist__albums div.album_selectable")
for i in popular_albums:
    if worship_group in i.text:
        print(f"{popular_albums.index(i)+1}. В популярном альбоме '{i.text}' в качестве исполнителя: '{worship_group}'")
    else:
        print("Альбом не совпал с артистом")

#Воспроизведение музыки
list_music = driver.find_elements(
    by=By.CSS_SELECTOR, value="div.page-artist__tracks_top img")
songs = [] # Список в который добавляются песни

for i in list_music:
    songs.append(i)

songs[0].click()

time.sleep(3)
"""
if driver.find_element(by=By.CLASS_NAME, value="MotionTailorHorizontal"):
    display = driver.find_element(by=By.CLASS_NAME, value="JqMWv").value_of_css_property("display")
    while display == "block":
        time.sleep(1)
else:
    print("Реклама не отображалась")
"""
#Проверка по иконке играет ли песня
playing_icon = 'url("https://music.yandex.by/i/YSQRtZPd9jSn4o0jrNgDPEtMWVg.svg")'
not_playing_icon = 'url("https://music.yandex.by/i/du6a-XlLXVHiaOUThuEY-dlyEFA.svg")'

def cheack_state():
    icons_music = driver.find_elements(by=By.CLASS_NAME, value="d-track__start-column")
    icon_state = icons_music[0].find_element(by=By.CSS_SELECTOR, value="button span.d-icon_play-small")
    if icon_state.value_of_css_property("background-image") == playing_icon:
        print("\nПесня играет")
    elif icon_state.value_of_css_property("background-image") == not_playing_icon:
        print("\nПесня не играет, на паузе")
    else:
        print(f"Непредвиденное условие - '{icon_state.value_of_css_property('background-image')}'")

cheack_state() # Проверка играет ли песня

actions.click(songs[0]).perform() # Остановка песни на паузу

time.sleep(3)
cheack_state() # Проверка на паузе ли песня

pass
