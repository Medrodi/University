import os
from converter import *
import PIL
def change_dir() -> None:
    """
    Функция 'change_dir' просит пользователя ввести новую директорию. Потом она проверяет, существует ли такая
    директория с помощью метода 'os.path.isdir'. Если такая директория существует, то рабочий каталог меняется
    на неё
    """
    dir = input(r"Укажите корректный путь к рабочему каталогу: ")
    if os.path.isdir(dir):
        os.chdir(dir)
    else:
        print("Ошибка, такой папки не существует!")
        change_dir()

def find_files(path: str, *expansions: str) -> list:
    """
     Функция `find_files` принимает параметр `path`, который является строкой представляющей путь к директории,
     а также параметр 'expansions', которые указывают файлы с каким расширением необходимо искать.
     Функция 'find_files' ищет файлы с указанными расшиерниями и возвращает список 'correct_files'

    :param path: путь к директории
    :param expansions: расширения, по которым будут искаться фалы
    :return: список файлом с нужными нам разрешениями
    """
    correct_files = []
    for exp in expansions:
        file_list = os.listdir(path)
        for file in file_list:
            if file[-(len(exp)):] == exp:
                correct_files.append(file)
    return correct_files

def find_pdf(path: str) -> None:
    """
    Функция `find_pdf` принимает параметр `path`, который является строкой представляющей путь к директории.
    Функция `find_pdf` сначала вызывает функцию 'find_files' с параметром '.pdf' и получает список
    файлов с расширеннием '.pdf'. Далее пользователь выбирает, перевести один файл или все из формата '.pdf'
    в формат '.docx'
    :param path: путь к директории
    """
    pdf_list = find_files(path, ".pdf")
    if len(pdf_list) == 0:
        print("В этом каталоге  нет .pdf файлов")
        return False
    print("Список файлов с расширением  .pdf")
    for i in range(len(pdf_list)):
        print(f"{i + 1}. {pdf_list[i]}")
    choice = input(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного "
                   "каталога введите 0): ")
    if int(choice) <= len(pdf_list):
        pdf_2_docx(os.path.join(pdf_list[int(choice) - 1]))
        print("Операция успешно выполнена")
    elif choice == '0':
        for i in range(len(pdf_list)):
            pdf_2_docx(os.path.join(pdf_list[i]))
        print("Операция успешно выполнена")
    else:
        print("Ошибка! Поробуйте ещё раз")

def find_docx(path:str) -> None:
    """
    Функция `find_docx` принимает параметр `path`, который является строкой представляющей путь к директории.
    Функция `find_docx` сначала вызывает функцию 'find_files' с параметром '.docx' и получает список
    файлов с расширеннием '.pdf'. Далее пользователь выбирает, перевести один файл или все из формата '.docx'
    в формат 'pdf'
    :param path: путь к директории
    """
    docx_list = find_files(path, ".docx")
    if len(docx_list) == 0:
        print("В этом каталоге нет .docx файлов")
        return False
    print("Список файлов с расширением  .docx")
    for i in range(len(docx_list)):
        print(f"{i + 1}. {docx_list[i]}")
    choice = input(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного "
                   "каталога введите 0): ")
    if int(choice) <= len(docx_list):
        docx_2_pdf(os.path.join(docx_list[int(choice) - 1]))
        print("Операция успешно выполнена")
    elif choice == '0':
        for i in range(len(docx_list)):
            docx_2_pdf(os.path.join(docx_list[i]))
        print("Операция успешно выполнена")
    else:
        print("Ошибка! Попробуйте ещё раз")

def find_pic(path: str) -> None:
    """
    Функция `find_pic` принимает параметр `path`, который является строкой представляющей путь к директории.
    Функция `find_pic` сначала вызывает функцию 'find_files' с параметроми '.jpeg', ".gif", ".png", ".jpg"
    и получает список файлов с этими расширенниями. Далее пользователь выбирает, сжать один файл или все файлы
    на определённый параметр сжатия, который выбирает пользователь. Также он выбирает названия для этих файлов
    :param path: путь к директории
    """
    pic_list = find_files(path, ".jpeg", ".gif", ".png", ".jpg")
    if len(pic_list) == 0:
        print('В этой папке нет картинок')
        return False
    print("Список файлов с расширением  .jpeg  .gif  .png  .jpg")
    for i in range(len(pic_list)):
        print(f"{i + 1}. {pic_list[i]}")
    choice = input(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного "
                   "каталога введите 0): ")
    if int(choice) <= len(pic_list):
        compress_pic(os.path.join(pic_list[int(choice) - 1]))
        print("Операция успешно выполнена")
    elif choice == '0':
        for i in range(len(pic_list)):
            compress_pic(os.path.join(pic_list[i]))
        print("Операция успешно выполнена")
    else:
        print("Ошибка! Попробуйте снова")
        find_pic(path)
