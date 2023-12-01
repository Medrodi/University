import os

from converter import *
from delete_files import *
from directories import *

def show() -> None:
    """
    Функция 'show'  позволяет пользователю взаимодействовать со всеми функциями пакета.
    Функция 'show' предоставляет выбор между функциями пакета, далее он выполняет выбранную функцию
    :return: None
    """
    while True:
        path = os.getcwd()
        print(f"\nТекущий каталог: {path}\n")
        print("Выберите действие:\n")
        print("0. Сменить рабочий каталог\n"
              "1. Преобразовать PDF в DOCX\n"
              "2. Преобразовать DOCX в PDF\n"
              "3. Произвести сжатие изображений\n"
              "4. Удалить группу файлов\n"
              "5. Выход\n")
        c = input("Ваш выбор: ")
        print()
        if c == '0':
            change_dir()

        elif c == "1":
            find_pdf(path)

        elif c == "2":
            find_docx(path)

        elif c == "3":
            find_pic(path)

        elif c == "4":
            delete(path)

        elif c == "5":
            break





if __name__ == "__main__":
    show()
