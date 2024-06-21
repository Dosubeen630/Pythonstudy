import csv

def getKey(item):  #정렬을 위한 함수
    return item[1]  #신경 쓸 필요없음

command_data = [] #파일 읽어오기
with open("command_data.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)

command_counter = {}    #dict 생성, 아이디를 key값 , 입력줄수 value값
for data in command_data: #list 데이터를 dict 타입으로 변경
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

dictlist = []
for key, value in command_counter.items():
    temp = [key,value]
    dictlist.append(temp)

sorted_dict = sorted(dictlist, key=getKey, reverse=True)
print(sorted_dict[:100])                       