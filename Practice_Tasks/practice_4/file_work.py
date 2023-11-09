def read_file(file):
    f = open(file, mode='r', encoding='utf-8')
    words = set()
    word_list = f.read().lower()
    word_list = word_list.replace(',', '').replace('—', ' ')

    for i in word_list.split():
        words.add(i)
    f.close()
    return sorted(words)


def save_file(list):
    length = len(list)
    print(f"Содержимое файла data.txt\n"
          f"Всего уникальных слов: {length}\n"
          f"======================")
    for i in list:
        print(i)

