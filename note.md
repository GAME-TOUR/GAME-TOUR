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

## 썸네일 
https://steamcdn-a.akamaihd.net/steam/apps/<APP_ID>/library_600x900_2x.jpg

게임별 고유 ID를 APP_ID에 넣으면 600*900 사진을 구할 수 있다. 

## gameDB MySQL TABLE
```sql
ID          int(10), 
title       varchar(50), 
studio      varchar(50), 
publisher   varchar(50), 
tag         varchar(50), 
game_info   TEXT NULL, 
platform    varchar(25)
```