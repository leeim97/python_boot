table = [[90,85,70],[88,79,92],[100,100,100],[90,60,70]]
print('---성적표 (점수)---')
for i in range(len(table)):
    print(table[i])

print('---성적표 (점수,총점,평균)---')
for score in table:
    print(f'{score} , {sum(score)} , +{(sum(score)/len(score)):.1f}')