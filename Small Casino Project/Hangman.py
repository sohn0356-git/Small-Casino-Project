import random
import requests
import time
from bs4 import BeautifulSoup

alphabet = []   # alphabet을 담고 있는 list(전역변수)
dict = []       # http://wordfind.co.kr/word-length로부터 불러온 단어를 저장하는 list(전역변수)

def user_input(n):
    """
        사용자로부터 알파벳을 입력받는다.
        알파벳 이외의 입력을 받을 경우 다시 입력받는다.
    """

    while True:
        ret = input("a~z까지 알파벳 하나를 입력하세요[%d회 miss] : "%n)
        if ret in alphabet and len(ret)==1:
            return ret.lower()

def init():
    """
        List alphabet에 a~z까지 추가한다.
        http://wordfind.co.kr/word-length 사이트에서
        6글자로 이루어진 영단어를 크롤링하여 dict에 저장한다.
    """
    if len(alphabet)==0:
        for i in range(ord('a'),ord('z')+1):
            alphabet.append(chr(i))
            alphabet.append(chr(i).upper())

    if len(dict)==0:
        print("단어를 생성하고 있습니다. 10~15초정도의 시간이 소요됩니다.")
        for i in range(1, 76, 5):
            url = "http://wordfind.co.kr/word-length/6-letters_" + str(i) + ".html"
            html_website_word = requests.get(url)
            soup_website_word = BeautifulSoup(html_website_word.content, 'html.parser', from_encoding='utf-8')
            website_words = soup_website_word.select('li.li1')
            for website_word in website_words:
                word = website_word.get_text()[:6]
                hint = website_word.get_text().split('}')
                if len(hint) == 2:
                    dict.append([word, hint[1]])

def play():
    """
        1. dealer는 영단어장에서 6자리 단어를 임의로 뽑는다.

        2. player에게 6천만원이 주어지고 게임이 시작된다.

        3. 게임은 player가 dealer의 단어를 맞출 때까지 진행된다.

        4. dealer는 뽑은 단어의 뜻을 사용자에게 힌트로 알려준다.

        5. player가 dealer의 단어를 추측하는 행위를 한 턴이라고 하자.

        6. 매 턴, player는 한 가지 알파벳을 말한다.

        7. 해당하는 알파벳이 dealer가 뽑은 단어에 있을 경우 player는 돈을 잃지 않는다.

        8. 없었을 경우 player는 1천만원을 잃게 된다.

        9. dealer는 뽑은 6글자의 단어의 각 자리를 적되 사용자가 여태까지 말한 적이 있는 알파벳이면

           공개하고 아니면 '_'을 기록한다.

           ex) dealer의 단어 : casino, 사용자가 말한 알파벳 : ['a, c, i, o']

           기록된 단어 : ca_i_o

    """
    init()
    award = 6
    cnt = 0
    target = random.randint(0,len(dict))
    target = dict[target]
    board = ['_']*6
    while True:
        print("Hint : "+target[1])
        user_alpha = user_input(cnt)
        for i in range(6):
            if board[i]=='_' and target[0][i]==user_alpha:
                board[i] = user_alpha
            print(board[i],end='')
        print()
        if '_' not in board:
            print("%d번 틀리고 정답을 맞추셨습니다. 상금은 %d천만원입니다"%(cnt, award))
            time.sleep(5)
            return award

        if user_alpha not in target[0]:
            cnt += 1
            award -= 1

play()