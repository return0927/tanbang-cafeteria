# -*- coding: utf-8 -*- 

import tCafeteria

cafe = tCafeteria.tCafeteria("G100000479")	#탄방중 학생코드
res = cafe.parseCafeteria()

w = open("./today.txt", "w")
today = w.write(res[1:len(res)-1])
w.close()