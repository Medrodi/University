from Monty_hall import *
from Birthday import *

def show():
    while True:
        print("\nВыберите функцию: ")
        print("1. Парадокс дней рождения \
              \n2. Парадок Монти Холла\n")
        c = input('Ваш выбор: ')

        if c == "1":
            birthday(int(input('Введите количество итераций: ')), int(input('Введите количество людей: ')))
        elif c == "2":
            monty_hall(int(input('Введите количество итераций: ')))
        else:
            break
if __name__ == "__main__":
    show()