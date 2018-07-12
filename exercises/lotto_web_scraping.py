from collections import OrderedDict

import csv  # import whole module
import requests  # import whole module
from bs4 import BeautifulSoup  # import only things that we need

URL = "http://www.lotto.pl/lotto/wyniki-i-wygrane"  # we can use both: single ' and double quotes "
HEADERS = (  # this is a tuple, created as a literal
    'Gra',
    'Numer losowania',
    'Data',
    'Dzien tyg',
    'Liczby',
    '',
)

html_doc = requests.get(URL)
html_doc.encoding = 'utf-8'

soup = BeautifulSoup(html_doc.text, 'html.parser')

data = list()

tabela = soup.find_all('table', class_="ostatnie-wyniki-table")[0]

for i, wiersz in enumerate(tabela.find_all('tr')):
    tmp_dict = OrderedDict()
    komorki = wiersz.find_all('td', recursive=False)
    for naglowek, komorka in zip(HEADERS, komorki):
        tmp_dict[naglowek] = komorka.text.strip()
    if tmp_dict:
        data.append(tmp_dict)

plik = open('wynik.csv', 'w')
writer = csv.writer(plik, delimiter='\t')
writer.writerow(HEADERS)

for wiersz in data:
    writer.writerow(tuple(wiersz.values()))

plik.close()

