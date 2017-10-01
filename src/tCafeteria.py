# -*- coding: utf-8 -*- 

# Copyright (c) 2017 w3bn00b
# See the file LICENSE for copying permission.
# tanbang-cafeteria v1.2
# author : w3bn00b
# description : 중학교의 급식정보와 학사일정 파싱해옵니다
# Usage : cafe = tCafeteria("학교코드", "관할지역 코드")
# Required library : datetime, bs4, requests

from datetime import *
from bs4 import BeautifulSoup
import requests



class tCafeteria:
	locale = 'DAEJEON'
	
	region = {
		'SEOUL':'stu.sen.go.kr',
		'INCHEON':'stu.ice.go.kr',
		'BUSAN':'stu.pen.go.kr',
		'GWANGJU':'stu.gen.go.kr',
		'DAEJEON':'stu.dje.go.kr',
		'DAEGU':'stu.dge.go.kr',
		'SEJONG':'stu.sje.go.kr',
		'ULSAN':'stu.use.go.kr',
		'GYEONGGI':'stu.goe.go.kr',
		'KANGWON':'stu.kwe.go.kr',
		'CHUNGBUK':'stu.cbe.go.kr',
		'CHUNGNAM':'stu.cne.go.kr',
		'GYEONGBUK':'stu.gbe.go.kr',
		'GYEONGNAM':'stu.gne.go.kr',
		'JEONBUK':'stu.jbe.go.kr',
		'JEONNAM':'stu.jne.go.kr',
		'JEJU':'stu.jje.go.kr'
	}
	
	def __init__(self, schoolcode, locale):
		self.schoolcode = schoolcode #학교코드 설정
		self.locale = locale
	
	def getDate(self):
	#	return datetime.today().day	#오늘 날짜
		return 12
	def getMonth(self):
	#	return datetime.today().month #달
		return 9
	def getYear(self):
		return datetime.today().year #연도
	
	def parseCafeteria(self):
		url = "http://"+self.region[self.locale]+"/sts_sci_md00_001.do?schulCode="+self.schoolcode+"&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=1"	#NEIS 학교급식 정보
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
	
	def parseSchedule(self):
		url = "http://"+self.region[self.locale]+"/sts_sci_sf00_001.do?schulCode="+str(self.schoolcode)+"&schulCrseScCode=3&schulKndScCode=03&ay="+str(self.getYear())+"&"+"mm="+str(self.getMonth())+"&"	#학사일정 링크
		r = requests.get(url)	#html코드를 불러온다
		soup = BeautifulSoup(r.text, "html.parser")
		
		allofsche = soup.find_all("td", attrs={"class":"textL"})	#class가 textL(학사일정)인 부분만 긁어온다
		
		res = str(allofsche[self.findIndex()].find("span"))
		
		#테그 제거
		if res == "None":
			res = allofsche[self.findIndex()]
			res = res.replace('''<td class="textL"''', "")
			res = res.replace("</td>", "")
		else:
			res = res.replace('''<span style="color:red">''', "")
			res = res.replace("</span>", "")
			res = res.replace("<span>", "")
		return res
		
	def findIndex(self):	#학사일정을 저장해둔 list에 index를 계산해준다
		if self.getMonth() >= 9 or self.getMonth() <= 2:
			if self.getMonth() >= 9:
				return (self.getMonth() - 9) + (self.getDate() - 1) * 6
			if self.getMonth() <= 2:
				return (self.getMonth() + 3) + (self.getDate() - 1) * 6
		if self.getMonth() >= 3 or self.getMonth <= 8:
			return (self.getMonth() - 6) + (self.getDate() - 1) * 6
