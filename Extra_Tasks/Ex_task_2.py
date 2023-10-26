a = {}
def mainscreen():
    print('Добро пожаловать в телефонную книгу! \
         \nСписок команд: \
          \n1. Добавить контакт\
           \n2. Удалить контакт (по имени) \
            \n3. Просмотреть телефонную книгу \
             \n4. Изменить номер телефона (по имени) \
              \n5. Выход \n')
    var(str(input('Введите номер команды: ')))
def proverka_number_in_items():
    number = create_number()
    if number in a.values():
        print('Данный номер принадлежит другому контакту!\n'
              'Введите другой номер \n')
        return proverka_number_in_items()
    else:
        return number
def create_number():
    n = str(input('Введите номер телефона: '))
    if len(n) in [11, 12]:
        if n[1:].isdigit():
            if len(n) == 12 and ((n[0] != '+') or (n[1] != '7') or (n[2] != '9')):
                print('Введён недостоверный номер телефона, попробуйте снова \n')
                return create_number()

            elif len(n) == 11 and (n[0] != '8' or n[1] != '9'):
                print('Введён недостоверный номер телефона, попробуйте снова \n')
                return create_number()

            elif len(n) == 11 and n[0] == '8' and n[1] == '9':
                n = n.replace('8', '+7', 1)
                return n
            elif len(n) == 12 and (n[0] == '+') and (n[1] == '7') and (n[2] == '9'):
                return n
        else:
            print('Введён недостоверный номер телефона, попробуйте снова: ')
            return create_number()
    else:
        print('Введён недостоверный номер телефона, попробуйте снова: ')
        return create_number()
def proverka_imeni():
    i = create_name()
    if i in a.keys():
        print('Контакт с данным именем уже существует! Выберите другое имя\n')
        return proverka_imeni()

    else:
        return i
def create_name():
    i = str(input('Введите имя и фамилию контакта: '))
    if len(i.split()) == 2:
            if i.split()[0].isalpha() and i.split()[1].isalpha():
                name = (i.lower().split())[0]
                username = (i.lower().split())[1]
                name = name.replace(name[0], name[0].upper(), 1)
                username = username.replace(username[0], username[0].upper(), 1)
                i = name + ' ' + username
                return i

            else:
                print('Введены некорректные данные! Попробуйте ещё раз\n')
                return create_name()
    else:
        print('Введены некорректные данные! Попробуйте ещё раз\n')
        return create_name()
def komanda_1():
    i = proverka_imeni()
    n = proverka_number_in_items()

    a[i] = n
    print('Новый контакт успешно добавлен!\n')
def komanda_2():
    i = create_name()
    if i in a.keys():
        del a[i]
        print('Контакт успешно удалён\n')
    else:
        print('Данного контакта нет в телефонной книге! \n'
              'Попробуйте ещё раз!\n')
        komanda_2()
def komanda_3():
    return print(f'{a} \n')
def komanda_4():
    i = create_name()
    if i in a.keys():
        n = proverka_number_in_items()
        a[i] = n
        print('Контакт успешно изменён\n')
    else:
         komanda_4()

def var(v):
    if v == '1':
        komanda_1()
        var(str(input('Введите номер команды: ')))
    elif v == '2':
        komanda_2()
        var(str(input('Введите номер команды: ')))
    elif v == '3':
        komanda_3()
        var(str(input('Введите номер команды: ')))
    elif v == '4':
        komanda_4()
        var(str(input('Введите номер команды: ')))
    elif v == '5':
        print('Всего доброго!')

    else:
        print('Данной команды не существует, попробуйте снова')
        var(str(input('Введите номер команды: ')))


mainscreen()
