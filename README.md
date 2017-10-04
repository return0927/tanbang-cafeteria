# tanbang-cafeteria

학교 급식정보와 학사일정을 파싱해옵니다

## Installation
```sh
from tCafeteria import *
```

tanbang-cafeteria 모듈은 bs4, requests를 필요로 합니다!
자동으로 모듈을 설치하는 메소드가 있지만,
작동하지 않으면 아래의 과정을 따라 수동 설치해주세요.
```sh
$ pip install bs4 requests
```
로 먼저 설치해주세요!
## 학교 구분 코드
```
# 관할지역 정보
# 'SEOUL':'stu.sen.go.kr',
# 'INCHEON':'stu.ice.go.kr',
# 'BUSAN':'stu.pen.go.kr',
# 'GWANGJU':'stu.gen.go.kr',
# 'DAEJEON':'stu.dje.go.kr',
# 'DAEGU':'stu.dge.go.kr',
# 'SEJONG':'stu.sje.go.kr',
# 'ULSAN':'stu.use.go.kr',
# 'GYEONGGI':'stu.goe.go.kr',
# 'KANGWON':'stu.kwe.go.kr',
# 'CHUNGBUK':'stu.cbe.go.kr',
# 'CHUNGNAM':'stu.cne.go.kr',
# 'GYEONGBUK':'stu.gbe.go.kr',
# 'GYEONGNAM':'stu.gne.go.kr',
# 'JEONBUK':'stu.jbe.go.kr',
# 'JEONNAM':'stu.jne.go.kr',
# 'JEJU':'stu.jje.go.kr'

# 학교 종류
# 'KINDERGARTEN':'1'
# 'ELEMENTARY':'2'
# 'MIDDLE':'3'
# 'HIGH':'4'
```

## Test Code
```py
from tCafeteria import *

cafe = tCafeteria("G100000479", 'DAEJEON', 'MIDDLE')	#탄방중 학교코드, 지역, 학교 종류(중학교)
res = cafe.parseCafeteria()
print(res)

res = cafe.parseSchedule()
print(res)
```

## Result
Example 1
```py
{"error":['정보가 없습니다','']}
추석
```
Example 2
```py
{'lunch': [['흑미밥(중등)', ''], ['돈육김치찌개(중등)', '5.9.10.13.'], ['달걀찜', '1.'], ['얼갈이된장무침', '5.6.'], ['치킨너겟', '1.2.5.6.13.'], ['깍두기(완)', '9.13.']], 'dinner': [['생야채불고기비빔밥', '5.6.10.'], ['쌀밥', ''], ['팽이버섯된장국', '5.6.9.13.'], ['라이스틱', '1.2.13.'], ['백김치(완)', '9.13.'], ['요구르트', '2.']]}

```

## License
MIT
```sh
# -*- coding: utf-8 -*-

# Copyright (c) 2017 w3bn00b, return0927
# See the file LICENSE for copying permission.
# tanbang-cafeteria v1.3
# started by : w3bn00b | re-arranged by : return0927
# description : 중학교의 급식정보와 학사일정을 파싱해옵니다
# Usage : cafe = tCafeteria("학교코드", "관할지역 코드")
# Required library : datetime, bs4, requests
```