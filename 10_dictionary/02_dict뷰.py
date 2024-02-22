# 뷰(view)
# 뷰는 딕셔너리 요소들을 동적으로 볼 수 있는 객체
#keys(), values(),items()

d = {'one':1,'two':2,'three':3}
# keys() 뷰
keys = d.keys()
print(keys,type(keys))

print(list(keys))

#  키(key)들에 대한 값(value)들을 출력
for key in d.keys():
    print(key,d[key])

# values() 뷰
values= d.values()
print(values,type(values),list(values))
print(len(values))

for value in d.values():
    print(value,end=',')
print()

# items() 뷰
items = d.items()
print(items,type(items))
print(list(items))

for item in d.items():
    print(item,type(item))

for key,item in d.items():
    print(key,item)

