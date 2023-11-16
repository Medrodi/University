import re
import csv

patern = r"(?:[А-я]{4}) (?P<number>[\d]{3}) (?:[А-я]+) (?P<city>[А-я]* [А-я]+)(?: . )(?P<time>\d{2}:\d{2}:\d{2})"
with open('data.txt', 'r', encoding='utf-8') as file:
    reader = file.read()

    match = re.findall(patern, reader)

with open('sorted_data.txt', 'w', encoding='utf-8', newline='') as file:
    for i in match:
        print(i)
        file.write(f"[{i[2]}] - Поезд №{i[0]} {i[1]}\n")

