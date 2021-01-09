import random

def input_num():
    """사용자로부터 중복되지 않는 숫자 4개를 입력받는다 """
    visited = [0] * 10
    ret = []
    try:
        user_num = input("0~9의 중복되지 않는 숫자 4개를 입력하시오 : ").split()
        for u in user_num:
            u = int(u)
            if 0 <= u and u <= 9 and visited[u]==0:
                visited[u]=1
                ret.append(u)
    except:
        print("다시 입력해주세요!")
    return ret

def gen_num():
    """ 0~9의 중복되지 않는 4개의 숫자를 임의로 배치하여 return 한다 """
    visited = [0]*10
    ret = []
    while len(ret)<4:
        next = random.randint(0,9)
        if visited[next]==0:
            visited[next] = 1
            ret.append(next)
    return ret

def play():
    """
        1. dealer는 중복되지 않는 0~9의 숫자 4개를 고르고 임의로 배열한다.

        2. player에게 1억의 돈이 주어지고 게임이 시작된다.

        3. 게임은 player가 dealer의 숫자를 맞출 때까지 진행된다.

        4. player가 dealer의 숫자를 추측하는 행위를 한 턴이라고 할 때

           player는 한 턴당 1천만원을 잃게 된다.

        5. 매 턴, player는 4자리 숫자를 추측한다.

        6. player가 추측한 4자리 숫자와 dealer가 정한 4자리 숫자를 비교한다

            1. 자리와 숫자가 일치할 경우 strike이다.
            2. 자리는 틀렸지만 player가 추측한 숫자가 dealer가 정한 숫자 중에 있을 경우 ball이다.
            3. 4 strike일 경우 게임이 끝나고 상금을 타게 된다.
            4. 아닐 경우 strike와 ball 카운트를 알려주고 턴이 끝난다.
    """
    award = 6
    answer = gen_num()
    cnt = 0

    print("\nLet's start\n")

    while True:
        print()
        print("현재 시도 횟수 : "+str(cnt))
        user_num = []
        while len(user_num)!=4:
            user_num = input_num()
        print(user_num)

        cnt_ball = 0
        cnt_strike = 0

        for i in range(4):
            if user_num[i]==answer[i]:
                cnt_strike += 1
            else:
                if user_num[i] in answer:
                    cnt_ball += 1

        if cnt_strike==4:
            print("Congratulation %d번만에 맞추셨습니다!"%cnt)
            return award-cnt
        else:
            print("%d Strike %d Ball" %(cnt_strike, cnt_ball))
        cnt += 1

play()