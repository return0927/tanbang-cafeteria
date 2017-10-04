# -*- coding: utf-8 -*- 

# Copyright (c) 2017 w3bn00b
# See the file LICENSE for copying permission.
# tanbang-cafeteria v1.3
# author : w3bn00b
# description : 중학교의 급식정보와 학사일정을 파싱해옵니다
# Usage : cafe = tCafeteria("학교코드", "관할지역 코드")
# Required library : datetime, bs4, requests

from datetime import *
from bs4 import BeautifulSoup
import requests, re

fetchDate = lambda: [datetime.today().year, datetime.today().month, datetime.today().day]

class tCafeteria:
    locale = 'DAEJEON'
    schType = 'MIDDLE'
    region = {
        'SEOUL': 'stu.sen.go.kr',
        'INCHEON': 'stu.ice.go.kr',
        'BUSAN': 'stu.pen.go.kr',
        'GWANGJU': 'stu.gen.go.kr',
        'DAEJEON': 'stu.dje.go.kr',
        'DAEGU': 'stu.dge.go.kr',
        'SEJONG': 'stu.sje.go.kr',
        'ULSAN': 'stu.use.go.kr',
        'GYEONGGI': 'stu.goe.go.kr',
        'KANGWON': 'stu.kwe.go.kr',
        'CHUNGBUK': 'stu.cbe.go.kr',
        'CHUNGNAM': 'stu.cne.go.kr',
        'GYEONGBUK': 'stu.gbe.go.kr',
        'GYEONGNAM': 'stu.gne.go.kr',
        'JEONBUK': 'stu.jbe.go.kr',
        'JEONNAM': 'stu.jne.go.kr',
        'JEJU': 'stu.jje.go.kr'
    }

    Type = {
        'KINDERGARTEN': '1',  # 병설유치원
        'ELEMENTARY': '2',  # 초등학교
        'MIDDLE': '3',  # 중학교
        'HIGH': '4'  # 고등학교
    }

    def __init__(self, schoolcode, locale, schType):
        self.schoolcode = schoolcode  # 학교코드 설정
        self.locale = locale
        self.schType = schType

    def getDate(self):
        return datetime.today().day

    def getMonth(self):
        return datetime.today().month

    def getYear(self):
        return datetime.today().year  # 연도

    def parseAlergic(self, data):
        p = re.compile("[0-9]+[.]") # 알레르기 표기 추출용 정규표현식
        alg = "".join(p.findall(data)) # 정규표현식으로 알레르기 정보 추출
        _temp = data.replace(alg, '')
        return [_temp, alg] # 알레르기 정보가 없으면 alg는 ''를 리턴

    def makeValue(self, tag):
        _TEMP = str(tag)[5:-6].split("<br/>")

        if "[석식]" in _TEMP[1:]: # 석식이 있는지 확인
            _INDEX = _TEMP[1:].index("[석식]")
            _Lunch = _TEMP[1:][:_INDEX]
            _Dinner = _TEMP[1:][_INDEX:]
            self.parseAlergic(_Lunch[1])
            return {
                "Date": _TEMP[0],
                "Data": [
                    {
                        "type": "Lun",
                        "data": [ self.parseAlergic(meal) for meal in _Lunch[1:]]
                    },
                    {
                        "type": "Din",
                        "data": [ self.parseAlergic(meal) for meal in _Dinner[1:]]
                     }
                ]
            }
        else:
            return {
                "Date": _TEMP[0],
                "Data": [
                    {
                        "type": "Lun",
                        "data": [ self.parseAlergic(meal) for meal in _TEMP[1:][1:] ]
                    }
                ]
            }

    def parseCafeteria(self, date=fetchDate() ):
        """
            function arguments:
            - date (Default: Now timestamp)

            : `date` arg type formation
            ['yyyy','m or mm','d or dd']
        """

        _YEAR, _MONTH, _DAY = date
        try:
            url = "http://%s/sts_sci_md00_001.do?schulCode=%s&schulCrseScCode=%s" + \
                  "&schulKndScCode=0%s&schMmealScCode=1&&ay=%d&mm=%d"
            url = url%\
                  (
                      self.region[self.locale],
                      self.schoolcode,
                      self.Type[self.schType],
                      self.Type[self.schType],
                      _YEAR,
                      _MONTH
                  )
            print(url)
            r = requests.get(url)
        except: # HTTP GET 오류 raise
            raise Exception("Error on getting server information")
        soup = BeautifulSoup(r.text, "html.parser")

        try:
            res = soup.select("#contents > div > table > tbody > tr > td > div")
            res = [ {"Date":tag.text, "Data":None} if tag.find("br") is None else self.makeValue(tag) for tag in res ]
        except: # 파싱 오류 raise
            raise Exception("Error on parsing data")

        return res

    def parseSchedule(self):
        url = "http://" + self.region[
            self.locale] + "/sts_sci_sf00_001.do?schulCode=" + self.schoolcode + "&schulCrseScCode=" + self.Type[
                  self.schType] + "&schulKndScCode=0" + self.Type[self.schType] + "&ay=" + str(
            self.getYear()) + "&" + "mm=" + str(self.getMonth()) + "&"  # 학사일정 링크
        print(url)
        r = requests.get(url)  # html코드를 불러온다
        soup = BeautifulSoup(r.text, "html.parser")

        allofsche = soup.find_all("td", attrs={"class": "textL"})  # class가 textL(학사일정)인 부분만 긁어온다

        res = str(allofsche[self.findIndex()].find("span"))

        # 테그 제거
        if res == "None":
            res = str(allofsche[self.findIndex()])
            res = res.replace('''<td class="textL"''', "")
            res = res.replace("</td>", "")
        else:
            res = res.replace('''<span style="color:red">''', "")
            res = res.replace("</span>", "")
            res = res.replace("<span>", "")
        res = res.replace("<", "")
        res = res.replace(">", "")
        return res

    def findIndex(self):  # 학사일정을 저장해둔 list에 index를 계산해준다
        if self.getMonth() >= 9 or self.getMonth() <= 2:
            if self.getMonth() >= 9:
                return (self.getMonth() - 9) + (self.getDate() - 1) * 6
            if self.getMonth() <= 2:
                return (self.getMonth() + 3) + (self.getDate() - 1) * 6
        if self.getMonth() >= 3 or self.getMonth() <= 8:
            return (self.getMonth() - 6) + (self.getDate() - 1) * 6
