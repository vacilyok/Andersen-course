import requests
from bs4 import BeautifulSoup


URL = "https://emojipedia.org/nature/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
emoji_elements = soup.find_all("li")

new_zoo = []
for elem in emoji_elements:
    try:
        elem.find("span", class_="emoji").text.strip()
        new_zoo.append(elem)
    except:
        pass

zoo = {}
for elem in new_zoo:
    animal = (elem.find("a").text.strip()).replace('/', '').replace('  ', '')
    animal_img = (animal.split(' ')[0]).strip()
    animal_name = ("".join(animal.split(' ')[1:])).strip()
    zoo.update({animal_name: animal_img})

print(zoo)
