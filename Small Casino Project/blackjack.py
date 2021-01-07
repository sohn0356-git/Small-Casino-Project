#Project :Black jack
#시나리오
#1. 무작위 카드 3장을 받는다.
#2. 받은 카드 중 합하여 21과 가장 가까운 카드를 선택하여 제출한다.
#3. 이후 딜러 카드와 비교하여 21 숫자와 가장 가까운 값을 낸 사람이 승리
#4. 승리할 경우 배팅 금액의 X2, 21일 경우 배팅 금액의 X4배
#5. 패배할 시 배팅 금액 0원
import random

user_card = []
dealer_card = []
dealerFinal_card = 0
userSel_card = []
temp_money = 0
UserMoney = 0
         
def cmp_value(): #최종 선택한 카드값과 딜러 카드값 비교
    global UserMoney
    global userFinal_card
  
    while True:
        try:
            userSel_card = input("가지고 있는 카드 중 두장을 선택하세요.").split(' ')
            for i in range (2) :
                userSel_card[i] = int(userSel_card[i])
            userFinal_card = sum(userSel_card)
            break
        except :
            print("숫자를 입력하시오")  
    
    print("나의카드: ",userFinal_card)
    print("딜러카드: ",dealerFinal_card)
    if userFinal_card > dealerFinal_card and userFinal_card != 21 :
        print("축하합니다! 게임에 승리하셨습니다.")
        UserMoney = UserMoney * 2
        print("획득 금액: ", UserMoney)
    
    elif userFinal_card == dealerFinal_card :
        print("게임에 비겼습니다.")
    
    elif userFinal_card < dealerFinal_card :
        print("게임에 패배하셨습니다.")
        UserMoney = 0
        print("획득 금액: ",UserMoney)

    elif userFinal_card == 21 :
        print("축하합니다! 게임에 승리하셨습니다.")
        UserMoney = UserMoney * 4
        print("획득 금액: ", UserMoney)

def Clear(): #게임을 한판 더 할 경우 변수 초기화한다.
    user_card.clear()
    dealer_card.clear()
    dealerFinal_card = 0

def continue_game(): #게임 진행 여부 묻는 코드
    flag = 0
    while True:
        opinion = input("한 판 더 진행하시겠습니까?(y/n)")
        if(opinion == 'y') :
            Clear()
            break
        elif opinion == 'n':
            print("고생하셨습니다.")
            flag = 1
            break
        else :
            print("y or n을 입력하시오")
    return flag
#-----------------------------------------------------------------------
print("블랙잭에 참여하신걸 환영합니다.")
def init_bet() :
    global UserMoney
    global dealerFinal_card
    while True: #베팅 정수 입력 예외 처리 및 딜러 카드 설정
        try:
            tmp_UserMoney =  input("얼마를 배팅하시겠습니까?")
            UserMoney += int(tmp_UserMoney)
            break
        except  ValueError:
            print("정수를 입력하시오")
    for i in range(2):
        dealer_card.append(random.randint(1,12))
    if(sum(dealer_card) < 12):
        dealer_card.append(random.randint(1,12))
    maximum = 21
    for i in range(len(dealer_card)) :
        for j in range(i+1, len(dealer_card)) :
            if dealer_card[i] + dealer_card[j] > maximum :
                continue
            else:
                dealerFinal_card = max(dealerFinal_card, dealer_card[i] + dealer_card[j])
#----------------------------------------------------------------------
def play() :
    global UserMoney
    global plus_card
    global dealerFinal_card
    global state
    global user_card
    while True : #Game Start
        init_bet()
        state = 0
        print("지금부터 카드 2장을 나눠드리겠습니다. ")
        dealer_card = []
        for i in range(2):
            user_card.append(random.randint(1,12))
            dealer_card.append(random.randint(1,12))
        user_card.sort(reverse=True)
        print(user_card) #가지고 있는 카드 보여주기

        if(sum(user_card) > 21) :
            print("카드 합이 21이 넘어 게임에 패배하셨습니다.")
            UserMoney = 0
            print("획득 금액: ", UserMoney)
            state = 1
            if continue_game() == 1 :
                break
 
        #딜러 카드가 12보다 작으면 카드 한장을 더 받아 21에 가깝도록 만든다.
        if(sum(dealer_card) < 12):
            dealer_card.append(random.randint(1,12))
        
        if(sum(dealer_card) > 21): #딜러 카드가 21이 초과될 경우 게임 승리
            print("딜러가 카드 합이 21일이 넘어 게임에 승리하셨습니다.")
            print("딜러 카드값: ", sum(dealer_card))
            UserMoney = UserMoney * 2
            state = 1
            print("획득 금액: ", UserMoney)
            if continue_game() == 1 :
                break   
        #-----------------------------------------------------------------------------
        #21에 가까운 dealer 카드 합 구하기
        maximum = 21
        for i in range(len(dealer_card)) :
            for j in range(i+1, len(dealer_card)) :
                if dealer_card[i] + dealer_card[j] > maximum :
                    continue
                else:
                    dealerFinal_card = max(dealerFinal_card, dealer_card[i] + dealer_card[j])
        #-----------------------------------------------------------------------------
        #사용자가 가지고 있는 카드가 21에 비해 부족하다면 카드를 한 장 더 받을지 선택하며
        #한장 더 받을 경우 받는 카드가 21을 넘어갈 경우 burst로 게임에 패배한다.
        plus_card = []
        if(state != 1) :  
            while True:
                plus_card = input('카드한장을 더 받겠습니까?(y/n)')
                if plus_card == 'y':
                    user_card.append(random.randint(1,12))
                    if(sum(user_card) > 21) :
                        print("Burst\n게임에 패배하셨습니다.")
                        UserMoney = 0
                        break
                    print(user_card)
                elif plus_card == 'n' : #카드를 받지 않으면 게임 포기
                    break
                else:
                    print("y or n을 입력하시오") #y or n 일때 예외 처리
        #-------------------------------------------------------------------------------
        #카드를 더이상 안받을 경우 Play the Game
        if(plus_card == 'n') :
            cmp_value()
        #-------------------------------------------------------------------------------
        if(state != 1) : 
            if continue_game() == 1: #게임을 더이상 하지 않으면 게임 종료
                break
play()








        




