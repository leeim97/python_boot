# with 문 : close()가 자동으로 수행
# with open(파일명, 모드) as 파일객체:
#       수행문장들
#
# with open('study_data2.txt','r') as f:
#     text=f.read()
#     print(text)
#
# with open('file1.txt','a',encoding='utf-8') as f:
#     f.write(text)

# with open('scores.txt','r',encoding='utf-8')as f:
#     data= f.readlines()
#     print(data)

with open('scores2.txt','r',encoding='utf-8')as f:
    data=f.readlines()
    print(data)