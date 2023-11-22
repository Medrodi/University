def get_data(file):
    with open(file, 'r', encoding='utf-8',) as file:
        data_list = []
        reader = file.readlines()
        for i in range(len(reader)):
            data_list.append(reader[i].strip().split('|'))

        return data_list

def get_books_python(list):
    list_with_python = []
    data_list = list
    for i in range(len(data_list)):
        if 'Python' in data_list[i][1]:
            list_with_python.append(data_list[i])
    print(list_with_python)

def get_total(list):
    data_list = list
    list_quantity_price = []
    for i in range(1, len(list)):
        if float(data_list[i][3]) * float(data_list[i][4]) < 500:
            list_quantity_price.append((data_list[i][0], float(data_list[i][3]) * float(data_list[i][4]) + 100))
        else:
            list_quantity_price.append((data_list[i][0], float(data_list[i][3]) * float(data_list[i][4])))
    print(list_quantity_price)
