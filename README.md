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

import tCafeteria

cafe = tCafeteria.tCafeteria("G100000479")	#탄방중 학생코드
res = cafe.parseCafeteria()

w = open("./today.txt", "w")
today = w.write(res)
w.close()
```

## License
MIT
