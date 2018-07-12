import requests
import hashlib
import time

import unicodecsv as csv

from bs4 import BeautifulSoup
from collections import OrderedDict
from lxml import html


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        method(*args, **kw)
        te = time.time()

        return '%2.2f sec' % (te - ts)

    return timed


HEADERS = (
    u'Nazwa funduszu',
    u'Kurs',
    u'Waluta',
    u'St. zw. 1D',
    u'St. zw. 7D',
    u'St. zw. 1M',
    u'St. zw. 3M',
    u'St. zw. 1R',
    u'St. zw. 3L',
    u'Data',
    u'Ranking 12M',
)

response = requests.get('http://www.bankier.pl/fundusze/notowania/wszystkie')
response.encoding = 'utf-8'

@timeit
def balor(response, filename):
    html_doc = response.text  # that's the decoded content of the response

    # parse the contents as a HTML
    soup = BeautifulSoup(html_doc, 'html.parser')
    # look for tables with specified class. Take the first one (0-based
    # indices).
    table = soup.find_all('table', class_='sortTableMixedData')[0]

    data = list()  # we could also write: data = []

    for row in table.find_all('tr'):  # take the data from one row at a time
        # we will extract the row data into this dictionary
        tmp_dict = OrderedDict()

        for header, cell in zip(HEADERS, row.find_all('td', recursive=False)):
            # recursive=False means: don't look for nested td's
            # "  XYZ\n\n \t".strip() == "XYZ"
            tmp_dict[header] = cell.text.strip()
        data.append(tmp_dict)  # add just processed row to our resulting list

    # open the file in binary writing mode (or create if not existing yet)
    f = open(filename, 'wb')

    # that's the guy that knows how to translate python objects to csv files
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)  # the headers have to be written manually

    for x in data:  # take each computed row
        w.writerow(x.values())  # {'a': 5, 13: 'lol'}.values() == (5, 'lol')
    # we have to close the file handler to make sure that the write buffer is
    # flushed
    f.close()