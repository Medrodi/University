def read_file(file):
    f = open(file, mode='r', encoding='utf-8')
    count_numbers = int(f.readline())
    numbers = []
    numbers_list = list(f.read().splitlines())
    print(numbers_list)


