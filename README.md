# tanbang-cafeteria

학교 급식정보를 파싱해옵니다

## Installation
```sh
$ pip install -e ./tCafeteria.py
```

tanbang-cafeteria 모듈은 bs4를 필요로 합니다!
bs4 모듈을 설치하지 않으셨다면
```sh
$ pip install bs4
```
로 먼저 설치해주세요!
## Test code
```sh
# -*- coding: utf-8 -*- 

# Copyright (c) 2017 w3bn00b
# See the file LICENSE for copying permission.
# example.py v1.0
# author : w3bn00b
# description : 학교 급식 정보를 파싱해와 이를 today.txt에 저장합니다
# Usage : cafe = tCafeteria("학교코드")
# Required library : datetime, bs4, requests

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

from tCafeteria import *

cafe = tCafeteria("G100000479", 'DAEJEON')	#탄방중 학생코드, 지역
res = cafe.parseCafeteria()

w = open("./today.txt", "w")
today = w.write(res)
w.close()
```

## License
MIT
