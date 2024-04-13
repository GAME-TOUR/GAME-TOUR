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
```sql
https://steamcdn-a.akamaihd.net/steam/apps/<APP_ID>/library_600x900_2x.jpg

-- 게임별 고유 ID를 APP_ID에 넣으면 600*900 사진을 구할 수 있다. 
```

## 크롤링한 데이터를 DB에 저장하기 
```
정형 데이터는 RDBS(MySQL)로 관리 
비정형 데이터(이미지)는 MongoDB로 관리 
파이썬과의 연동을 위해 pymysql 라이브러리 사용 
```
### gameDB Column Type 
```sql
-- tag를 text 형식으로 저장하기 위해 배열 자료형을 문자열로 변환, 호출 시 다시 파싱하여 배열로 사용 

id INT(11),
title varchar(50),
studio varchar(50),
publisher varchar(50),
tag TEXT NULL,
info TEXT NULL,
platform varchar(25)
```

## MODIFY
```sql
-- 개발사/배급사 이름이 길어 '+'로 처리되어있는 게임들이 있다. 예외처리 해야함 Ex. 이터널 리턴 
```