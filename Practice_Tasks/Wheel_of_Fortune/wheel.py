import random

def next_time():
    print('Хотите сыграть ещё раз?')
    print('1. Да\n'
          '2. Нет')
    k = input('Ваш выбор:')
    if k == '1':
        return 1
    if k == '2':
        return 0
def choice_difficult(a):
    if a == '7':
        return ' | ♥x7'
    elif a == '5':
        return ' | ♥x5'
    elif a == '3':
        return ' | ♥x3'
def read(path = 'words.txt'):
    a = [str(x) for x in open('words.txt', 'r', encoding='utf-8').readlines()]
    a = [line.rstrip() for line in a]
    return a

def game(t):
    record = 0
    a = read()
    word = random.choice(a)
    word_hunt = '*' * len(word) + choice_difficult(t)
    print(word)
    true = True
    while true == True:

        print(word_hunt)
        s = str(input('Назовите букву или слово целиком: '))
        proverka = []
        if s == word:
            print('Вы выиграли')
            yn = next_time()
            if yn == 1:
                true = False
                game(t)
            else:
                true = False


        if word_hunt[:len(word)] == word:
            print('Вы выиграли')
            true = False

        elif s in word:
            for i in range( len(word)):
                if s == word[i]:
                    proverka.append(i)
            for i in proverka:
                word_hunt = word_hunt[:i] + s + word_hunt[i + 1:]





game('7')
