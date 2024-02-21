# 반복문 for

# 1~10사이의 정수를 더하기

sum=0
for i in range(1,11):
    sum+=i

print(sum)

# 1부터 10사이의 홀수 더하기

sum=0
for i in range(1,10,2):
    sum+=i

print(sum)

# 값을 시작값, 끝값을 입력받아 이 사이에 있는 정수 더하기

start=int(input())
end= int (input())

sum=0
for i in range(start,end+1):
    sum+=i

print(sum)
    
# 5명의 점수 입력받아 합격 >=60, 불합격 <60 출력
for _ in range(5):
    score=int(input('0~100 사이의 점수 입력: '))
    if score >= 60:
        print(f'{score}합격')
    else:
        print(f'{score}불합격')
