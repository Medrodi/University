# название организации ---- адрес ---- номер телефона ---- часы работы
import re
import csv
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

adres_request = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()

pattern = (r'(?:org-widget-header__title-link">)(?P<names>[^<]+)(?:[^9]+)(?:location">\s+)(?P<adres>[^<]+\b)(?:[^0-9]+)(?:spec__value">)(?P<mubers>.[^<]+)(?:[^0-9,]+)(?:[^0-9,]spec__value">)(?P<time>[^<]+)')


match = re.findall(pattern, adres_request)



print(match)

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Adres', 'Phone', 'Work Time'])

    for i in match:
        print(i)
        writer.writerow(i)

