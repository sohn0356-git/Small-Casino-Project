# Small Casino Project



## 개요

* 1조의 첫 팀 프로젝트
* 각자 `Python`을 사용하여 한 개 이상의 게임을 만들고 그 게임들을 모아서 *Small Casino*를 개장해보았다.
* 5가지 [게임](#게임)이 존재하고 추후에 더 추가될 수도 있다.



## 팀원

* 김현수



* 손경주
  * 사용가능 언어 : Python, Java, C++
  * 취미 : 운동, 독서, 영화
  * 개발분야 : Embedded System, Android App Develop
  * Blog : [sohn0356-git.github.io](https://sohn0356-git.github.io)
  * Contact : sohn0356@naver.com



* 한상범



* 한재영



## Rule

* 카지노와 비슷한 환경을 조성하기 위해 모든 게임은 베팅시스템이 존재한다.
* 게임을 시작하면 5천만원이 주어지고 원하는 게임을 플레이하며 돈을 잃을 수도 있고 얻을 수도 있다.
  * 단, 가진 돈이 0원 혹은 그 밑으로 떨어질 경우 카지노에서 추방된다.



## 게임

### Bulls and Cows <img src="./md-images/baseball.png" height = "80" width="80">
#### * 개발자 : 경주

* 게임 설명 : 흔히 숫자야구라고 불리며 dealer가 random하게 제시한 4개의 숫자를 player가 맞추는 게임이다.
* 게임 방식 :

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



### Hangman <img src="./md-images/rope.png" height = "80" width="80">

#### * 개발자 : 

* 게임 설명 : dealer가 임의의 영어 단어를 제시하면 player가 맞추는 게임이다.

* 게임 방식 :

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



### Coin Toss <img src="./md-images/coin.jpg" height = "80" width="80">

#### * 개발자 : 

* 게임 설명 :



### Number Guess <img src="./md-images/number.jpg" height = "80" width="80">

#### * 개발자 : 

* 게임 설명 :



### Blackjack <img src="./md-images/blackjack.jpg" height = "80" width="80">

#### * 개발자 : 

* 게임 설명 :