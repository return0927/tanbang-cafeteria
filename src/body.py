import tCafeteria

funcSc = tCafeteria.tCafeteria("G100000202","DAEJEON","HIGH")
#funcSc = tCafeteria.tCafeteria("G100000479", 'DAEJEON', 'MIDDLE')
response = [
    funcSc.parseCafeteria(),
    funcSc.parseSchedule()
]
print(response[0][9])