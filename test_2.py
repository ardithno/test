import requests
from bs4 import BeautifulSoup

n = 0
animals  = dict()
url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text

while n!=5000:
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
    for name in names:
        animals[name.text[0].upper()] = animals.get(name.text[0].upper(), 0) + 1
        n+=1
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text

for key, value in animals.items.sorted():
    print(f'{key}: {value}')