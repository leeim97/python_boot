num= int(input("학생 수 입력 : "))

scores=[]
total=0
cnt=0
for i in range(num):
    scores.append(int(input(f'학생{i} 점수 입력 : ')))
    total+= scores[i]
    if scores[i] >= 80:
        cnt+=1

print(f"총점 : {total}")
print(f"평균 : {total/num:.2f}")
print(f"80점 이상 학생 : {cnt}명")

