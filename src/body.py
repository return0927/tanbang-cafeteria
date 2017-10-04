import tCafeteria

funcSc = tCafeteria.tCafeteria("G100000202","DAEJEON","HIGH")
#funcSc = tCafeteria.tCafeteria("G100000479", 'DAEJEON', 'MIDDLE')
response = [
    funcSc.parseCafeteria(),
    funcSc.parseSchedule()
]

for _dict in response[0]:
    print(_dict)