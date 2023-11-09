def read():
    text = open('words.txt', 'r', encoding='utf-8')
    text_list = text.read().lower().splitlines()
    text.close()
    return text_list

def get_record(record):
    record_file = open('records.txt', mode ='r+', encoding='utf-8')
    cur_record = record_file.readline()
    if int(record) > int(cur_record):
        record_file.seek(0)
        record_file.write(str(record))
        record_file.close()
        print(f"\nВы побили рекорд.\nВаш новый рекорд:{record}")
    else:
        record_file.close()
        print(f"\nВы не побили свой рекор.\nВаш текущий рекорд: {cur_record}")
