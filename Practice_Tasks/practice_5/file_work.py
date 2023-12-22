
def read_file(file):
    f = open(file, mode='r', encoding='utf-8')
    count_numbers = int(f.readline())
    numbers = []
    numbers_list = list(f.read().splitlines())
    int_numbers = []
    for i in range(numbers):
        int_numbers.append(int(i))

    print(numbers_list)


def Try():
    try:
        file_name = input('Введите название файла: ')
        read_file(file_name)

    except TypeError:
         print("Проверь тип данных")

    except FileNotFoundError:
        print("Данного файла не существует")

    except OSError:
        print("Ошибка операционной системы")

    except ValueError:
        print("Проверь символы в файле")

    except:
        print("Произошла непредвиденная ошибка!")


if __name__ == "__main__":
    Try()