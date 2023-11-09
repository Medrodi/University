import wheel as wheel
from data import *
def show():

    print('Добро пожаловать на Поле Чудес')
    print('Выберите сложность игры')
    print('\n1. Легкая\n'
            '2. Средняя\n'
            '3. Сложная\n')
    c = input('Ваш выбор: ')
    if c == '1':
        wheel.game('7', read(), 0)

    if c == '2':
        wheel.game('5', read(), 0)

    if c == '3':
        wheel.game('3', read(), 0)





if __name__ == '__main__':
    show()
