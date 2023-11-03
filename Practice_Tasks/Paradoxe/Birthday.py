import random
def birthday(count, countpeople):
    win = 0
    for t in range(count):
        a = []
        k = 0
        for i in range(countpeople):
            s = (str(random.randrange(1, 29)) + str(random.randrange(1, 13)))
            a.append(s)

        for i in range(len(a)):
            for r in range(1 + i, len(a)):
                if a[i] == a[r]:
                    k += 1
        if k > 0:
            win += 1
    print(f"\nкол-во итераций: {count}\nкол-во удачных случаев: {win}\nпроцент удачных случаев: {win / count * 100}%")