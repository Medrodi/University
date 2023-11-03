from wheel import *
def show():
    while True:
        print('Добро пожаловать на Поле Чудес')
        print('Выберите сложность игры')
        print('\n1. Легкая\n'
              '2. Средняя\n'
              '3. Сложная\n')
        c = input('Ваш выбор: ')
        if c == '1':
            game('7')

