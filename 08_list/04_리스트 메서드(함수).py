# 리스트 메서드 (함수)

#1. append():리스트 맨 뒤에 항목을 추가

a=[]
a.append('apple')
a.append('hotdog')
a.append(10)
print(a)

#2. pop(index):리스트의 맨 마지막 요소를 반환하고 요소를 제거
# 맨 마지막 값이 디폴트
value = a.pop()
print(f'alist : pop적용 {a},value={value}')
a.append('melon')
print(f'alist {a}')
print(f'alist : a.pop(0) {a.pop(0)}, pop 적용 후 {a}')

#3. sort() : 리스트의 요소들을 정렬하여 정렬된 리스트로 변경
#sort(reverse = True)하면 내림차순으로 정렬
b= [6,3,5,1,-3]
print(f'blist : {b}')
b.sort()
print(f'sort 적용 후 {b}')
#3.1 sort(key=str.lower)
char = ['b','B','A','a','z']
print(f'charList: {char}')
char.sort(key=str.lower)
print(f'charList sort.(key=str.lower): {char}')

#4. reverse() : 리스트를 역순으로 변경
#오름차순 내림차순,즉 정렬이 아니라 그냥 역순(거꾸로)
b.reverse()
print(b)

#5. index() : 리스트에서 지정한 값의 위치를 반환
c= ['홍길동','강감찬','성춘향','변학도','강감찬']
print(c.index('강감찬')) #강감찬 두개여도 처음본거
# 값이 없는 경우 valueError 발생
# ex) print(c.index('원빈'))

#6. insert(위치, 값) : 리스트에 요소 삽입
print(f'insert 전 {c})')
c.insert(-1,'원빈')
print(f'insert 후 {c})')
c.insert(2,'피카소')
print(f'insert 후 {c})')

#7. remove(값) : 리스트에서 지정한 값을 제거
print(f'remove 전 {c})')
#젤 첫번째 만나는 것만 지움
c.remove('강감찬')
print(f'c.remove("강감찬") 후 {c})')

#9. extend() : 리스트에 리스트를 추가(확장)
#하나의 리스트로 변경
print(f'blist {b}')
b.extend([10,11,12])
print(f'b.extend([10,11,12]) {b}')
#[10,11,12]를 append와 insert하면 리스트로 추가됌
# append,insert는 형식 그대로 추가되는듯
#[6, 5, 3, 1, -3,[10, 11, 12]]

# b.extend(100)하면 오류남 리스트 객체로 들어가야됌
# print(f'b.extend([10,11,12]) {b}')

#10. sorted() 내장 함수 : 리스트를 정렬한
# 새로운 리스트 반환 (기존 리스트 값 변환 X)
a=[3,1,-10,11,2]
print(f'alist {a}')
new_a=sorted(a,reverse = True)
print(f'sorted()함수 적용 후 alist {a}')
print(f'sorted()함수 적용 후 new_a {new_a}')

#11. copy() : 리스트 복사
cpy_a=a.copy()
print(cpy_a)
cpy_a.sort()
print(cpy_a)

#12. clear() : 리스트를 비우기

cpy_a.clear()
print(cpy_a)

#13. del() : 리스트 요소 지우기,리스트 전체를 지우기
#메모리 자체를 삭제 시킴
cpy_a=[1,2,3,4,5,6]
del(cpy_a[3:])
print(cpy_a)
del cpy_a #cpy_a는 메모리에서 삭제

#14. len() : 리스트의 길이를 반환
print(len(a))

#15. max() : 최대값을 반환하는 내장함수
#16. min() : 최소값을 반환하는 내장함수

ex_list = [100,7,-2,99,38]
x_list = ['shit','hello','Exit','zoo','hi']
print(ex_list)
#리스트에 숫자 문자열 섞여있는 경우 max,min처럼 비교 못함
print(f'최댓값{max(x_list)}')
print(f'최소값{min(x_list)}')

# 17. in, not in 연산자 : 리스트 내 원소 존재 여부 True/False 반환

num = [1,2,3,4,5]
result = 1 not in num
print(result)

#18. > < >= <= == != : 리스트 일치 검사
list1 = [1,2,3]
list2 = [1,3,2]
print(list1 <= list2)

