
n=4
total=00
num_list=[]
for i in range(n):
    num=int(input(f'{i+1}숫자입력: '))
    num_list.append(num)
    total += num

avg= total/4
print(f'합계: {total},평균 :{avg}')
print('num_list= ',num_list     )