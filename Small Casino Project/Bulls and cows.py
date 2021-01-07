import random

# 369게임
# 1. 중복되지 않는 4가지 숫자를 입력받는다.
# 2. 사용자로부터 숫자를 4개 입력받는다.
# 3. 369게임의 규칙에 맞게 결과를 출력한다.
# 4.

def input_num():
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
    """ 1~45의 중복되지 않는 6개의 숫자 list를 return """
    visited = [0]*10
    ret = []
    while len(ret)<4:
        next = random.randint(0,9)
        if visited[next]==0:
            visited[next] = 1
            ret.append(next)
    return ret

def play():
    """ """
    while True:
        answer = gen_num()
        cnt = 0
        print(answer)

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
            else:
                print("%d Strike %d Ball" %(cnt_strike, cnt_ball))

            cnt += 1


