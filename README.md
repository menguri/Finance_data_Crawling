# 주가 매수 흐름 크롤링 프로그램

## [개발 동기]<br>
기업의 주가 매수 흐름을 파악하고자 했다. 어떤 상황 속에서 어떤 집단이 매수하고, 어떤 집단이 매도하는지 알고자 했다. 
<br>

## [크롤링 대상]<br>
KRX / 정보데이터시스템
http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd
<br>

## [개발 언어]<br>
Python
<br>

## [크롤링 대상]<br>
1. 날짜
2. 총매수
3. 기업 매매
4. 개인 매매
5. 외국인 매매
6. PER
7. PBR
8. 외국인 비율
9. 가격
10. 요일
<br>


## [주의할 점]<br>
chromedriver 로 크롤링을 하기에, chromedriver와 사용자가 쓰고 있는 chrome 버전이 일치해야 돌아간다.
<br>
<br>
<br>

## [실행 파일 만드는 방법]<br>

(1) 초기 실행 파일 만들기 <br>
![image](https://user-images.githubusercontent.com/58064919/170482360-09f0bdd4-1834-4092-8697-dbb873f96628.png)

(2) 생성된 gui.spec 파일 고쳐주기 (기존에 있던 spec 파일은 지워주세요.)<br>
![image](https://user-images.githubusercontent.com/58064919/170482510-d98f476a-02fb-45b5-8317-8d300168469e.png)

(3) 마지막으로 합쳐주기 <br>
![image](https://user-images.githubusercontent.com/58064919/170481391-44dce8b7-be37-40bf-8566-1e51f9e17145.png)
<br>
<br>

## [실행 이미지]<br>

(1) 원하는 기업, 경로, 파일 유형, 기간을 설정해서 Continue를 누르면 진행됩니다.<br>
![image](https://user-images.githubusercontent.com/58064919/170482943-bc0f4905-cff3-4534-844d-db562dc7cc4d.png)
<br>


(2) <br>
![image](https://user-images.githubusercontent.com/58064919/170482747-1023a44c-a060-448b-a6a9-ef8c717735ec.png)
<br>

(3) <br>
![image](https://user-images.githubusercontent.com/58064919/170482821-4722f9bc-367a-4282-be89-17b0a4c52446.png)

