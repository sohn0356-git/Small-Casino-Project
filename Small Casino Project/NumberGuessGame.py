def p1_play():
    #1~ 99까지의 숫자 중 무작위로 하나를 선택합니다.
    import random
    number = random.randrange(1, 100)
    print("랜덤게임~ game start")
    award = 3000
    # 1부터 99까지 숫자를 입력 하되 100이상이거나 0이하인 수를 제외합니다.
    while True:
        guess = input('소주병뚜껑 숫자 맞히기 : 1부터 99까지., 숫자를 한 개 입력해보세요~~?, ( q 를 입력하면 게임이 종료됩니다.)')

        if guess == "q":
            print("게임을 종료합니다.")
            break
        elif guess != "q":
            print("잘못된 값을 입력하셨습니다.")
            continue

        if int(guess) >= 100 or int(guess) <=0:
            print("잘못된 값을 입력하셨습니다.")
            continue

        '''숫자를 맞추게 되면 1000만원을 획득하고, 틀릴 시에는 500만원을 차감합니다.
            사용자가 입력한 숫자가  정답보다 클 경우 down을 말해 값을 내리라고 말해줄 것이며
            사용자가 입력한 숫자가 정답보다 작을 경우 up을 말해 값을 더 키우라고 합니다.
            총 남은 금액을 합산해 상금으로 획득하게 됩니다.'''

        while True:
            if int(guess) == number:
                award += 1000
                print("{0} 만원을 획득하셨습니다.\nGG\n축하합니다!!!".format(award))
                break

            if int(guess) > number:
                    print("DOWN")
                    award -= 500
                    print()
                    print("남은 금액: {0} 만원".format(award))
                    break

            elif int(guess) < number:
                    print("UP")
                    award -= 500
                    print()
                    print("남은 금액: {0} 만원".format(award))
                    break

            return award


p1_play()