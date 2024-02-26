# csv(comma seperated value) 파일 읽기
# csv 모듈 임포트
# https://docs.python.org/ko/3/library/csv.html
import csv

# csv.reader
path='scores2.csv'
with open(path,'r',encoding='utf-8') as f:
    data = csv.reader(f)
    for x in data:
        print(x)

# obj= csv.writer(csvfile,delimeter(구분자))
# obj.writerows(사용할 데이터) : csv파일에 쓸 객체
# 데이터
data_list=[['구','전체','내국인','외국인'],
           ['관악구',519864,502089,17775],
           ['강남구',547602,542498,5014],
           ['송파구',686181,679247,6934],
           ['강동구',428547,424235,4312]]

with open('pop.csv','w',encoding='utf-8',newline='')as f:
    obj=csv.writer(f,delimiter=',')
    obj.writerows(data_list)

