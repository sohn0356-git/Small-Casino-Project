import Blackjack
import Bulls_and_Cows
import Hangman
import NumberGuessGame


user_money = 5

def start_game():
    global user_money
    """
        사용자에게 다음과 같은 선택지를 제시합니다.
        1. Play Blackjack Game
        2. Play Bulls and Cows Game
        3. Play Hangman Game
        4. Play Number Guess Game
        5. Quit Casino
    """

    while True:
        award = 0
        menu = input("무엇을 하시겠습니까? \n\n1. Play Blackjack Game\n2. Play Bulls and Cows Game\n3. Play Hangman Game\n4. Play Number Guess Game\n5. Quit Casino\n")

        if menu == "1":
            award = Blackjack.play()
        elif menu == "2":
            award = Bulls_and_Cows.play()
        elif menu == "3":
            award = Hangman.play()
        elif menu == "4":
            award = NumberGuessGame.play()
        elif menu == "5":
            print("무엇이든 적당히 할 때 가장 즐거운 법입니다. 좋은 시간이셨기를 바랍니다")
            break
        else:
            print("다시 입력해주세요 : ")
            continue
        user_money += award
        print("\n\n\n")
        print("현재 당신의 재산은 %d천만원입니다!" % user_money)



def main():
    """
        1조의 첫 팀 프로젝트
        각자 Python을 사용하여 한 개 이상의 게임을 만들고 그 게임들을 모아서 Small Casino를 개장해보았다.
        5가지 게임이 존재하고 추후에 더 추가될 수도 있다.
    """
    print("1조의 Small Casino에 오신 것을 환영합니다. 즐거운 시간 되세요~")
    print("현재 당신의 재산은 %d천만원입니다!" % user_money)
    start_game()




if __name__ == "__main__":
    main()