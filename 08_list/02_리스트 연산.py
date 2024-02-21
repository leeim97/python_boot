#1. 인덱싱(indexing) : 요소 접근

a=[0,1,2,3,4]
b=[[1,2],3,[5,6]]
print(a[0],a[-1],a[3])
print(b[0],b[2],b[0][0])

#2. 슬라아싱(slicing) : 부분 문자열
print('a[:]',a[:])
print('a[1:]',a[1:])
print('a[:2]',a[:2])
print('a[::2]',a[::2])
print('a[::-1]',a[::-1])

#3. 리스트 값 변경
print('변경전 a list',a)
a[1]= 100
print('변경 후 a list',a)
a[2]=[10,20]

#슬라이싱을 이용
print('변경 후 a list',a)
a[1:3]=[30,40]
print('변경전 a list',a)

#리스트를 각각의 변수에 넣기
c= [10,20,30]
x,y,z=c
print(x,y,z)


#4. 리스트 합치기:+  같은 리스트 자료형이니까 덧셈가능
a=[1,2,3,4]
b=[7,8,[9,10]]
print('a+b',a+b)

#5. 리스트 곱하기(반복) *
print('a*3',a*3)

#6. 리스트 복사(copy) : 깊은 복사 vs 얉은 복사
a= 10
b= a
print(a,b)
a_list= [10,20,30,40]
b_list = a_list  # shallow copy(얕은 복사) 한쪽이 바뀌면 다른 것도 바뀜
#리스트는 복사되지 않고 주소값만 복사하기 때문에 원본에 영향을 준다


print('alist',a_list,'blist',b_list)
a_list[0]='apple'
print('alist',a_list,'blist',b_list)
b_list[-1]='banana'
print('alist',a_list,'blist',b_list)
print(id(a_list),id(b_list))

#해결 방법
#deep copy

a_list= [10,20,30,40]
c_list=list(a_list) #새로운 리스트 만들고 a_list의 값을 써라
print('alist',a_list,'clist',c_list)
a_list[0]='apple'
print('alist',a_list,'clist',c_list)
c_list[-1]='banana'
print('alist',a_list,'clist',c_list)
print(id(a_list),id(c_list))
