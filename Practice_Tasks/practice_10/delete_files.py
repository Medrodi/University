import os

def delete_files(path: str) -> None:
    """
    Функция `delete_files` принимает параметр `path`, который является строкой представляющей путь к директории.
    Функция 'delete_files' предоставляет пользователю выбрать, по какому критерию будут удалены файлы. Далее
    функция 'delete_files' выполняет удаление необходимых файлов с помощью метода 'os.remove'
    :param path: путь к директории в формате строки
    :return: None
    """
    print("Выберите действие: ")
    print(f"1. Удалить все файлы начинающиеся на определённую подстроку\n"
          f"2. Удалить все файлы заканчивающиеся на определённую подстроку\n"
          f"3. Удалить все файлы содержащие определённую подстроку\n"
          f"4. Удалить все файлы по расширению\n")
    choice = input("Ваш выбор: ")
    
    if choice == "1":
        strka = input("Введите подстроку: ")
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                if file.startswith(strka):
                    os.remove(os.path.join(root, file))
                    print("Файл успешно удалён")
    elif choice == "2":
        strka = input("Введите подстроку: ")
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                if file.endswith(strka):
                    os.remove(os.path.join(root, file))
                    print("Файл успешно удалён")
    elif choice == "3":
        strka = input("Введите подстроку: ")
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                if strka in file:
                    os.remove(os.path.join(root, file))
                    print("Файл успешно удалён")
    elif choice == "4":
        strka = input("Введите расширение: ")
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                if file.endswith(strka):
                    os.remove(os.path.join(root, file))
                    print("Файл успешно удалён")
    else:
        print("Ошибка! Попробуйте ещё раз")
        delete_files()

def delete(path: str) -> bool:
    '''
    Функция `delete` принимает параметр `path`, который является строкой представляющей путь к файлу или директории.
    Функция `delete` проверяет, существует ли файл или директория по указанному пути с помощью метода `os.path.exists`.
    Если указанный путь не существует, то функция возвращает `False`.
    Если путь существует, то выполнение передается функции `delete_files`, которая удаляет файлы

    :param path: Путь к объекту в формате строки
    :return: True - в случае успешного удаления объекта. Во всех остальных случаях - False.
    '''
    if not os.path.exists(path):
        return False

    delete_files(path)
    return True