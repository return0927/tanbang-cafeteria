# -*- coding: utf-8 -*- 

# tanbang-cafeteria v1.0
# author : w3bn00b
# description : 대전 학교의 급식 정보를 파싱해옵니다
# Licence : GNU General Public License v3.0
# Usage : cafe = tCafeteria("학교코드")
# Required library : datetime, bs4, requests

from datetime import *
from bs4 import BeautifulSoup
import requests

class tCafeteria:
	def __init__(self, schoolcode):
		self.schoolcode = schoolcode	#학교코드 설정
	
	def getDate(self):
		return datetime.today().day	#오늘 날짜
	
	def parseCafeteria(self):
		url = "http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode="+self.schoolcode+"&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=1"	#NEIS 학교급식 정보
		r = requests.get(url)
		soup = BeautifulSoup(r.text, "html.parser")
		
		allofcafe = soup.find(id="contents")	#id가 content인 부분을 return
		table = soup.find("table")				#table 태그부분을 return
		tbody = table.find("tbody")				#tbody만 return
		td = tbody.find_all("td")				#td(급식메뉴)속 값을 list로 받음
		div = td[self.getDate() - 1].find_all("div")	#오늘의 급식
		
		res = str(div)
		res = res.replace("<div>", "")			#태그 제거
		res = res.replace("</div>", "")
		res = res.replace("<br/>", "\n")
		return str(res[1:len(res)-1])