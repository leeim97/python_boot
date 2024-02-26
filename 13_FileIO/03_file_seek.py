# seek(offset, whenen) 함수

print('파일 내에서 검색: seek() ----')
f= open('seek_test_data.txt','r',encoding='utf-8')

# f.seek(0,0)  #시작 위치:0, 0:파일 처음
# lines= f.readlines()
# print(lines)

#f.seek(1,0)  #시작 위치:1, 0:파일 처음
#f.seek(7,0)  #시작 위치:7, 0:파일 처음
f.seek(14,0)  #시작 위치:7, 0:파일 처음
lines= f.readlines()
print(lines)

f.close()