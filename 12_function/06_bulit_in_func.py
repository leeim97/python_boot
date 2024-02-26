# 내장함수들

# abs()
print(abs(-10))

# all(iterable) : 모두 True인 경우 True
# any(iterable) : 하나라도 True인 경우 True

# chr(): 숫자(아스키코드 넘버) 넣으면 해당되는 문자 리턴
# ord(): 문자 넣으면 해당하는 숫자(아스키코드) 리턴
#divmod(),pow()
# min(),max(),sum()

# round(number,소숫점이하 자리수) : 반올림
print(round(3.141592,2))

# enumerate(): 인덱스값을 포함한 enumerate객체 반환
print(list(enumerate(['kim','lee','choi'])))
# 인덱스와 값이 튜플 형태로 나온다
data=['kim','lee','choi']
for idx,value in enumerate(data):
    print(idx,value)

# eval(표현식): 표현식을 그대로 실행

print(eval('10'))
print(eval('10*10'))
print(eval('10'+'10'))

# filter() : 반복가능한 자료에 함수를
# 적용하여 True인 결과때 값을 추출!!
def positive(x):
    return x>0

def even(x):
    if x%2 ==0:
        return x

print(positive(10))
print(positive(-10))

print(list(map(positive,[1,2,-1,10,-5])))
print(list(filter(positive,[1,2,-1,10,-5])))

print(list(filter(even,[1,2,-1,10,-5])))

# help(): 도움말 시스템 호출
# help(print)
# help(filter)

# int(), float(), str()
# bin(), hex(), oct()
# input(), print()
# zip(), map()
# range()
# len()
# list(), tuple(), dict(), set()
# id(), type()
# lambda
