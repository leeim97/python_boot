# 텍스트파일 읽기
# read는 한번에 모두
# readline 한줄씩


# 텍스트파일 생성 : 메모장을 이용해서
# study_data.txt :한글
# study_data2.txt:영문

#한글 파일 ->디폴트가 cp949로 되있어서 한글파일은 utf-8해줘야됌ㅁ
#ANSI 코드로 저장하면 encoding='utf-8' 안해도됌

# 1단계: 파일열기(open)
f = open('study_data.txt',mode='r',encoding='utf-8')
# 2단계 : 파일처리(읽기)
text=f.read()
print(text)
# 3단계 : 파일닫기(close())
f.close()

# ★영문 파일
# 1단계: 파일열기(open)
# 파일객체를 리턴한다.
f1 = open('study_data2.txt',mode='r')

# 2단계 : 파일처리(읽기)
# 파일을 읽은것을 넣는다

# ★ text=f1.read()
# ★ text=f1.readline()
# print(text)
# text2=f1.readline()
# print(text2)
# text3=f1.readline()
# print(text3)

# ★ readline()
# while True:
#     text=f1.readline()
#     if not text: #읽을 내용이 없으면(마지막)
#         break
#     print(text)

# ★ readlines 쓰기
# for textline in f1.readlines():
#     print(textline)

# ★ readlines없이 그냥 file 객체에서 읽기
for textline in f1:
    print(textline)

# 3단계 : 파일닫기(close())
f1.close()


# seek() : 내 탐색 위치 지정

