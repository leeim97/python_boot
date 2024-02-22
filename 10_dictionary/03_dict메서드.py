# 1. get() 메서드

d= {'one':1,'two':2,'three':3}

print(f"d['two']:{d['two']}")
print(f"d.get('two') :{d.get('two')}")

# print(d['four']) # keyerror 발생 : 없는키 접근
print(d.get('four')) #key가 없는 경우 None 반환
print(d.get('four',4)) #key가 없는 경우 4 반환
#get은 four가 추가가 안되고 걍 4가 반환되는거고
#setdefault는 four 없으면 key four가 추가됌


# 2.setdefault() 메서드
#지정한 키가 있으면 그 값나오고
#없으면 키에 해당하는 값 추가됌
print(d)
d.setdefault('two')
d.setdefault('four',4)
print(d)

# 3.pop(),popitem() 메서드
print(d.popitem())
key,value=d.popitem()
print(f"key={key},value={value}")
print(d)

d['six']=6
d['ten']=10
print(d)
# pop은 무조건 키를 지정해야됌
result=d.pop('two')
print(result)
print(d)

# 4. copy()
d2 = d.copy()
print(d,id(d))
print(d2,id(d2))
# print(d)
# print(d2)

# 5. update() 뒤에 추가됌 다만 key가 이미 있다면
# 있는건 추가안됌
d3={'five':5,'two':2,'seven':7}
print(d3)
d3.update(d2)
print(d3)

# 6. clear()
# 딕셔너리 깔끔하게 다 없앰 기존 주소는 그대로
print(id(d))
d.clear()
print(id(d))

print(id(d))
d= {}
print(id(d))
