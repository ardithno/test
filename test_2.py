import requests
from bs4 import BeautifulSoup
import string

flag = True
animals  = dict()
url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text

while flag:
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
    for name in names:
        if name.text[0] == 'A':
            flag = False
            break
        if name.text[0].upper() == 'Ё':
            animals['Е'] += 1
            continue
        animals[name.text[0].upper()] = animals.get(name.text[0].upper(), 0) + 1
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text

for key in sorted(animals):
    if key in string.ascii_uppercase:
        continue
    print(f'{key}: {animals[key]}')