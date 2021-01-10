import random

def play():
    #1~ 99까지의 숫자 중 무작위로 하나를 선택합니다.

    number = random.randrange(1, 100)
    print("랜덤게임~ game start")
    award = 10

    # 1부터 99까지 숫자를 입력 하되 100이상이거나 0이하인 수를 제외합니다.

    while True:
        guess = input('소주병뚜껑 숫자 맞히기 : 1부터 99까지., 숫자를 한 개 입력해보세요~~?, ( q 를 입력하면 게임이 종료됩니다.)')

        if guess == "q":
            print("게임을 종료합니다.")
            break

        elif not guess.isdecimal() :
            print("잘못된 값을 입력하셨습니다.")
            continue

        guess = int(guess)

        if guess >= 100 or guess <= 0:
            print("잘못된 값을 입력하셨습니다.")
            continue


        if  guess == number:
            award += 20
            print("{0}천만원을 획득하셨습니다.\nGG\n축하합니다!!!".format(award))
            return award


        if  guess > number:
            print("DOWN")
            award -= 2
            print()
            print("현재 상금: {0}천만원".format(award))
            continue

        elif guess < number:
            print("UP")
            award -= 2
            print()
            print("현재 상금: {0}천만원".format(award))
            continue


