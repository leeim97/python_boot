# open() 의 'w'모드는 파일이 존재하는 경우 엎어쓰기

# 1.문자열을 파일에 쓰기
# s='''01234
# abcde f
# 가나다라마바'''
#
# f=open('write_data.txt','w',encoding='utf-8')
# f.write(s)
# f.close()

# #2. 키보드로 입력받은 문자열을 파일에 쓰기
# s= input('문자열 입력:')
# f= open('write_data2.txt','w',encoding='utf-8')
# f.write(s)
# f.close()

# 3.기존 파일 뒤에 추가 파일 쓰기: 'a'모드 사용
# s= input('문자열 입력: ')
s1 = '''1행
2행
3행
'''
f= open('write_data2.txt','a',encoding='utf-8')
f.write(s1)
f.close()

# 4. 파일을 생성(쓰기)하고 읽기

filename='readwrite.txt'
f=open(filename,'a',encoding='utf-8')
for i in range(5):
    f.write(f' {i}번째'+input(f'{i}번째 문자열 입력'))
f.close()

f2=open(filename,'r',encoding='utf-8')
print(f2.read())
f2.close