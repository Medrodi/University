import random
def monty_hall(count):
    winwithvv = 0
    winwithoutvv = 0

    for i in range(count):
        win = random.randrange(1,4)
        choose = random.randrange(1,4)

        viborved = random.randrange(1, 4) # ведущий открывает дверь и предлагает изменить выбор
        while viborved == choose or viborved == win:
            viborved = random.randrange(1, 4) #ведущий открывает дверь другую
        yn = random.randrange(0,2)
        if yn == 1:
            choose = 6 - choose - viborved
            if choose == win:
                winwithvv += 1

        elif yn == 0:
            if choose == win:
                winwithoutvv += 1

    sumaw = winwithvv + winwithoutvv
    print(f"\nкол-во побед: {sumaw}")
    print(f"кол-во побед при согласии с ведущим {winwithvv / sumaw * 100}")
    print(f"кол-во побед при несогласии с ведущим {winwithoutvv / sumaw * 100}")

