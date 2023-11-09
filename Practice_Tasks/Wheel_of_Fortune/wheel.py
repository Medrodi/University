import random
from data import *
def next_time():
    print('Хотите сыграть ещё раз?')
    print('1. Да\n'
          '2. Нет')
    k = input('Ваш выбор:')
    if k == '1':
        return 1
    if k == '2':
        return 0



def game(lifes, word_list, record):
    record = record
    word_list = word_list

    if word_list == []:
        print("Вы отгадали все слова! Поздравляю!")
        get_record(record)


    else:
        word = word_list.pop(random.randrange(len(word_list)))
        count_lifes = int(lifes)
        word_hunt = '*' * len(word)


        while True:
            print(f"{word_hunt} | ♥x{count_lifes}")
            s = str(input('Назовите букву или слово целиком: '))
            proverka = []

            if s == word:
                print('Вы выиграли')
                record += 1
                break

            if s in word:
                for i in range( len(word)):
                    if s == word[i]:
                        proverka.append(i)
                for i in proverka:
                    word_hunt = word_hunt[:i] + s + word_hunt[i + 1:]
            else:
                print('\nОшибка! Наверное, вы ввели не ту букву, или она уже есть в слове'
                      '\n-1 жизнь')
                count_lifes -= 1

            if word_hunt == word:
                print(f"Вы выиграли. Загаданное слово: {word}\n")
                record += 1
                break


            if count_lifes == 0:
                print('Ваши жизни закончились! Вы проиграли')
                get_record(record)
                break


        if count_lifes != 0:
            next_game = next_time()
            if next_game == 1:
                game(lifes, word_list, record)
            else:
                get_record(record)
                print('До новых встреч!')
        else:
            print("До новых встреч")




