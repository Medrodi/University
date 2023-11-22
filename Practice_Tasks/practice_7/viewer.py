from get_data import *

def show():
    print('Добро пожаловать')
    print('Выберите необходимую функцию\n'
          '1) получить список книг со словом python\n'
          '2) получить список с суммой * цену')
    c = input('Ваш выбор: ')
    if c == '1':
        get_books_python(get_data('books.csv'))
    elif c == '2':
        get_total(get_data('books.csv'))
    else:
        print('Ошибка данных')
