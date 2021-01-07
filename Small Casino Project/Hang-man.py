import random
import requests
import time
from bs4 import BeautifulSoup

alphabet = []

def user_input(n):
    while True:
        ret = input("a~z까지 알파벳 하나를 입력하세요[%d회 miss] : "%n)
        if ret in alphabet and len(ret)==1:
            return ret.lower()

def init():
    """"""
    for i in range(ord('a'),ord('z')+1):
        alphabet.append(chr(i))
        alphabet.append(chr(i).upper())

def play():
    init()
    userMoney = 0
    award = 6
    cnt = 0
    dict = []
    print("단어를 생성하고 있습니다. 10~15초정도의 시간이 소요됩니다.")
    for i in range(1,76,5):
        url = "http://wordfind.co.kr/word-length/6-letters_"+str(i)+".html"
        html_website_word = requests.get(url)
        soup_website_word = BeautifulSoup(html_website_word.content,'html.parser',from_encoding='utf-8')
        website_words = soup_website_word.select('li.li1')
        for website_word in website_words:
            word = website_word.get_text()[:6]
            hint = website_word.get_text().split('}')
            if len(hint)==2:
                dict.append([word,hint[1]])
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
            userMoney += award
            time.sleep(5)
            break

        if user_alpha not in target[0]:
            cnt += 1
            award -= 1


play()