import requests
from bs4 import BeautifulSoup
import csv
import os

URL = "https://auto.ria.com/newauto/marka-volkswagen/"
HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "accept":"*/*"
}
HOST = "https://auto.ria.com"
FILE = "cars.csv"
def get_html(url,params=None):
    req = requests.get(url,headers=HEADERS,params=params)
    return req


def get_pages_count(html):
    soup = BeautifulSoup(html, "html.parser")
    pagination = soup.find_all("span", class_="mhide")
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all("a", class_="proposition_link")
    #print(len(items))
    cars = []
    for i in items:
        uah_price = i.find("div", class_="proposition_price").find("span", class_="size16")
        if uah_price:
            uah_price = uah_price.get_text()
        else:
            uah_price = "Цены нет"
        cars.append({
            "title":i.find("h3", class_="proposition_name").get_text(strip=True) + " " + i.find(
                "div", class_="proposition_equip").get_text(strip=True),
            "link": HOST + i.get("href"),
            "usd_price": i.find("div", class_="proposition_price").find("span", class_="green").get_text(strip=True),
            "uan_price": uah_price,
            "city": i.find("div", class_="proposition_information").find("span", class_="item region").get_text(strip=True),

        })
    return cars

def save_file(items,path):
    with open(path,"w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Марка", "Ссылка", "Цена в долларах", "Цена в грн.", "Город"])
        for i in items:
            writer.writerow([i['title'], i['link'], i['usd_price'], i['uan_price'], i['city']])


def parse():
    URL = input("Введите URL:")
    html = get_html(URL)
    if html.status_code == 200:
      cars =[]
      pages_count = get_pages_count(html.text)
      for i in range(1,pages_count + 1):
          print(f"Парсинг страницы {i} из {pages_count}...")
          html = get_html(URL,params={"page":i})
          cars.extend(get_content(html.text))
      save_file(cars,FILE)
      print(f"Получено {len(cars)} автомобилей")
      os.startfile(FILE)
    else:
        print("Error")

parse()

