if __name__ == '__main__':
    path = '../Wheel_of_Fortune/words.txt'

def get_words(path = r"C:\PycharmProjects\University\Practice_Tasks\test_wheel\words.txt"):
    text = open(path, encoding= 'utf-8')
    text_list = text.read().upper().splitlines()
    text.close()
    return text_list

def get_records(record, path = r"C:\PycharmProjects\University\Practice_Tasks\test_wheel\records.txt"):
    record_file = open(path, mode = 'r+', encoding='utf-8') #ctrl + пробел
    cur_record = record_file.readline()
    cur_record = max(int(cur_record), int(record))
    record_file.seek(0)
    record_file.write(str(cur_record))
    return cur_record

# if __name__ == '__main__':
#     path = '../Wheel_of_Fortune/words.txt'
#     get_words(path)
#     print(get_words(path))
#     get_records(10)

print(dir())
print(__file__) #брать из файла и замени ть после последнего слеша поменять на ИМЯ текстового файла

