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

# 문제점
nintendo 설명문 저장 시 특수문자가 들어가 cp949를 쓰면 한글이 깨진다. 근데 UTF-16 형식을 사용하면 항목별로 저장이 안되고 한 인덱스에 전부 저장됨