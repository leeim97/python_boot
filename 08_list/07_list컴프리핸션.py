# 리스트 컴프리핸션
#리스트 =[문장 for 변수 in 반복범위 [if 조건식]]

# num_list=[]
# for num in range(1,6):
#     num_list.append(num)

num_list = [ num for num in range(1,6)    ]
print(num_list)

num_list2 = [num*2 for num in range(1,6)]
print(num_list2)

num_list3 = [num**2 for num in range(1,6)]
print(num_list3)

# 문제. 1~20의 정수 중 짝수만으로 구성된 리스트 생성

n_list = [i for i in range(1,21) if i %2==0]
print(n_list)

foods=['a','b','c','d']
sides=['A','B','C']
#zip(객체) 구조는 리스트의 같은 인덱스에
#있는거를 묶어준다 따라서 d는 안묶임
for food,side in zip(foods,sides):
    print(food,'---',side)

for item in zip(foods,sides):
    print(item)

print(type(zip(foods,sides)),zip(food,sides))
print(list(zip(foods,sides )))

name=['cho','lee','son','hwang']
sex=['man','man','women','woman']
addr=['s','a','s','a']
print(list(zip(name,sex,addr)))