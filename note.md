# 필요한 정보

```
게임 한글/영문 이름 
개발사 / 배급사 
태그 
썸네일 (IMG) - 얘는 MongoDB를 이용하여 따로 관리
발매일 
게임 소개글 
플랫폼
스크린샷 ?? 
```
## 게임 목록 페이지 크롤링

```
I.   스크롤 전의 페이지 전체 높이 값 파악
II.  페이지 스크롤 
III. 스크롤 후의 페이지 전체 높이 값 파악
IV.  스크롤 전과 스크롤 후의 페이지 값 비교
V.   같지 않다면 스크롤 반복 else 스크롤 중지  
```

0406 스팀 게임 리스트 페이지 크롤링 구현, 출시일 elements를 수집하지 못하는 오류 발생

## 상세 페이지 게임 정보 크롤링 
```
I. 게임 이름 (무결성 체크)
II. 개발 스튜디오 / 배급사 
III. 태그 - 장르와 게임을 대표할 수 있는 단어들 수집
IV. 게임 설명 
```
# TO-DO 
## 썸네일 
```
https://steamcdn-a.akamaihd.net/steam/apps/<APP_ID>/library_600x900_2x.jpg

게임별 고유 ID를 APP_ID에 넣으면 600*900 사진을 구할 수 있다. 
```
## 크롤링한 데이터 하나로 합치기
```
[Steam] 게임목록과 게임 상세페이지 정보 합치기 
```

## DB에 저장하기 
```
정형 데이터는 RDBS(MySQL)로 관리 
비정형 데이터(이미지)는 MongoDB로 관리 
파이썬과의 연동을 위해 pymysql 라이브러리 사용 
```
### gameDB Column Type 
```sql
id INT(11),
title varchar(50),
studio varchar(50),
publisher varchar(50),
tag JSON,
info TEXT NULL,
platform varchar(25)
```

## 한국어 + 영어 게임 리스트 (94,470)
http://store.steampowered.com/search/?sort_by=Price_ASC&category1=998


## PROBLEM

~~개발사/배급사 이름이 길어 '+'로 처리되어있는 게임들이 있다. 예외처리 해야함 Ex. 이터널 리턴~~     
&rarr; 이름 태그 긁는거라 상관없었다. 

~~스팀 게임목록 스크롤 중 DLC도 받아오는거 예외처리해야함.~~   
&rarr; 필터에서 게임만 검색 체크 시 해결 가능 

~~여러게임이 합쳐진 합본이 있다. 예외처리해야함~~   
&rarr; tag가 none이면 파싱안하고 continue 

셀레니움 성능이 좋지 않아 2500개 크롤링하는데도 자꾸 먹통이 된다...

