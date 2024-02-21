# 리스트 삭제

a=[10,20,30]
b=[1,2,3]
c=['apple','coconut','melon','hotdog']

#1)리스트의 한 값을 삭제
print(f'삭제전 alist: {a}')
del(a[1])
print(f'삭제 후 alist: {a}')

print(f'삭제전 blist: {b}')
b[1:2]=[]
print(f'삭제 후 blist: {b}')

#2) 리스트 자체를 삭제
a.append(50)
b.append(5)
print(f'삭제 전 alist : {a}')
a=[]
print(f'삭제 후 alist : {a}')
print(f'a type : {type(a)}')

print(f'삭제 전 blist : {b}')
b=None #None도 타입 유형(정해지지 않았다라는 타입)
print(f'삭제 후 blist : {b}')
print(f'b type : {type(b)}')

print(f'삭제 전 clist : {c}')
del(c) #메모리에서 제거해버림
#c를 이제 쓸 수 없음
# print(f'삭제 후 clist : {c}')->오류뜸
# print(f'c type : {type(c)}')