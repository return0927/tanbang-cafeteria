# -*- coding: utf-8 -*- 

# Copyright (c) 2017 w3bn00b
# See the file LICENSE for copying permission.
# example.py v1.0
# author : w3bn00b
# description : 학교 급식 정보를 파싱해와 이를 today.txt에 저장합니다
# Usage : cafe = tCafeteria("학교코드")
# Required library : datetime, bs4, requests

import tCafeteria

cafe = tCafeteria.tCafeteria("G100000479")	#탄방중 학생코드
res = cafe.parseCafeteria()

w = open("./today.txt", "w")
today = w.write(res)
w.close()