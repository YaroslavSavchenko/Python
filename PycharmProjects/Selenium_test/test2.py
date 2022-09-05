import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestSelenium(unittest.TestCase):
    def test1(self) -> None:
        driver = webdriver.Chrome()

        # Отображение какой-то страницы
        driver.get("http://www.tutorialsninja.com/demo/")

        # Поиск елемента
        elem_search = driver.find_element(by=By.NAME, value="search")
        # Отправить в элемент ввода какие-то нажатия(тоесть текст)
        elem_search.send_keys("Iphone")