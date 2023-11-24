import pymorphy3
from translate import Translator
import csv
def get_data(file):
    with open(file, 'r', encoding='utf-8') as file:
        reader = file.read().split()
        data_list = []
        for i in reader:
            if i.isalpha():
                data_list.append(i)

    return data_list
def morph(list):
    words = list
    morph = pymorphy3.MorphAnalyzer()
    morphed_words = []
    for i in range(len(words)):
        morphed_words.append(morph.parse(words[i])[0].normal_form)
    return morphed_words

def count(list):
    words = list
    counted_words = {}
    for i in range(len(words)):
        counted_words[words[i]] = words.count(words[i])
    sorted_words = []
    for i in set(sorted(counted_words.values())):
        for r in counted_words.keys():
            if str(i) in str(counted_words[r]):
                sorted_words.append((r, counted_words[r]))
    sorted_words.reverse()
    return sorted_words

def translating(list):
    words = list
    print(len(words))
    translated_list = []
    progress = 0
    translator = Translator(from_lang="ru", to_lang="en")
    for i in range(len(words)):
        translation = translator.translate(words[i][0])
        translated_list.append((words[i][0], translation, words[i][1]))
        progress += 1
        print(f"{progress} из {len(words)}")
    return translated_list

def write_to_file(list):
    words = list
    with open("Translated_word.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Исходное слово|Перевод|Количество упоминаний"])
        for i in range(len(words)):
            writer.writerow([f"{words[i][0]}|{words[i][1]}|{words[i][2]}"])









if __name__ == '__main__':
    write_to_file(translating(count(morph(get_data("data.txt")))))