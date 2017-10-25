from tCafeteria import *
import tweepy

cafe = tCafeteria("G100000479", 'DAEJEON', 'MIDDLE')	#탄방중 학교코드, 지역(대전), 학교 종류(중학교)
meal = cafe.parseCafeteria()

# Dictionary+list형식의 return값을 하나의 문자열로 변환
try:
	print(meal['error'][0])
except KeyError:
	for i in range(len(meal['lunch'])):
		res = meal['lunch'][i][0] + " " + meal['lunch'][i][1]
		print (res)

