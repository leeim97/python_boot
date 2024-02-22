# 복수개 자료 치환
a,b=1,2
print(a,b,type(a),type(b))

#튜플이지만 swap에는 각각 변수 형태라 교환되서 가능하다
# 패킹 언패킹이라 생각?
a,b=b,a
print(a,b)

(a,b),(c,d)= (10,11),(12,13)
print(a,b,c,d)

# 패킹(packing) 여러개를 왼쪽 변수에 대입
t=1,2,'hello'
print(t)

# 언패킹(unpacking) 오른쪽 튜플을 풀어서 왼쪽에 대입
x,y,z = t
print(type(t))
print(x,y,z,type(x),type(y),type(z))

t2=(1,2,3,4,5)
a,b,*c = t2 #*를 붙히면 여러개의 요소를 갖고있다고 생각
#예를들어 리스트
#a에 한개 b에는 한개 c는 리스트니까 3,4,5
print(a,b,c,type(a),type(b),type(c))
# *a,b,c = t2는 됌
# *a,*b,c = t2는 안됌
