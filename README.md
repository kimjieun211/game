**### 프로젝트에 대한 소개**

<br>속도가 계속해서 증가하는 테트리스시간이 흐르면서, 레벨이 증가함에 따라, 자기가 증가시키면서 속도가 증가할 수 있다특히 레벨이 올라갈수록 속도는 기하급수적으로 증가하게 된다. <br>
오픈된 소스(‘Tetromino')를 사용<br>

**## 기능**

기본테트리스기능-7개 모양의 블록이 랜덤으로 내려온다-블럭이 쌓인다-블럭이 회전한다-블럭이 보드 위에 닿게되면 게임이 종료된다정지기능블록 자동 밑으로 내리기양방향으로 회전가능게임나가기
## **추가기능**

속도 증가- 시간이 흐름에 따라 속도가 증가- 레벨이 올라감에 따라 속도가 증가 (레벨 = 점수/10)- 사용자가 U키를 이용해서 속도를 증가 

**### 요약 및 매뉴얼**

![](http://postfiles5.naver.net/MjAxNzA2MTVfMjkg/MDAxNDk3NTAwNTkxMTk3.M3QVoHoSbn2Fv9ycbv17a6sxpdQK5uIO86LD4c7DBQMg.ozIASHyFLgTG2KGGGJ02yUgWKS814COw9iLqsOoIMR0g.JPEG.kimjieun211/%EC%8B%9C%EC%9E%91%ED%99%94%EB%A9%B4.JPG?type=w2)

테트리스 시작 화면: 아무키나 누르면 게임이 시작된다.
![](http://postfiles7.naver.net/MjAxNzA2MTVfMzIg/MDAxNDk3NTAwNTYwMjEy.2v_O0iyJVWLTrlx3qdSAnOG_Ikf-11_HjrP5msjZHOwg.XSbd_mGMjWH5p1GeQ9RtnppZv_s-9A0l-ccbaOCTj2Ug.JPEG.kimjieun211/ffff.JPG?type=w2)

테트리스 게임화면<사용 매뉴얼>-방향키나 ASD키로 왼쪽 아래 오른쪽으로 이동가능-Q키 : 왼쪽으로 회전-W키 : 오른쪽으로 회전-SPACEBAR : 블록 자동 밑으로 내리기-P키 : 게임정지-ESC키 : 게임나가기-U키 : 게임 속도 증가 

![](http://postfiles15.naver.net/MjAxNzA2MTVfMjg2/MDAxNDk3NTAwNTYxMTcw.sgQD_Ufj4sLir4PKjG-kA759UpszGhWHx568IQh809Qg.gqtaVhzlTamCZBJzkz6lpbGADBCpDvYNjJjUndngV6Mg.JPEG.kimjieun211/hjjk.JPG?type=w2)

게임 정지화면

![](http://postfiles7.naver.net/MjAxNzA2MTVfODYg/MDAxNDk3NTAwNTYwODA2.rUhqAnOwtB4mLKB0bTtECCgAVl85-MTRvBvQXal6Yj8g.AtqpvEug9X5mGGOTSJG0cTu7KD41Fwle-WytM1v3LMUg.JPEG.kimjieun211/ghj.JPG?type=w2)

게임오버 화면

**### 알고리즘 설명**

블록모양을 array로 나타낸다.블록모양은 random함수를 써서 randomg하게 나타나게 한다.
빈곳을 .으로 블록이 있는 부분을 0으로 나타내어isValidPosition함수를 통해 충돌체크하고충돌이 일어나지 않으면 그 위치로 이동한다.
이동은 키를 누름에 따라 x나 y를 증가시킴으로써 이동한다.
한 줄이 가득찬 선을 제거하고 위에 있는 것을 아래로 이동한다.한 줄이 가득찬 선을 제거하고 위에 있는 것을 아래로 이동한다.
