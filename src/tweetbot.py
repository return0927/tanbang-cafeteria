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

consumerKey = ""
consumerSecret = ""
 
#auth.OAuthHandler 객체 반환
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
 
accessToken = ""
accessTokenSecret = ""
 
#auth.OAuthHandler r객체에 엑세스토큰 지정
auth.set_access_token(accessToken, accessTokenSecret)
 
#API 클래스의 인스턴스 반환 - 읽기, 트윗, 리트윗, DM
api = tweepy.API(auth)
 
#트윗포스트
tweet = str(res)
api.update_status(status=tweet)