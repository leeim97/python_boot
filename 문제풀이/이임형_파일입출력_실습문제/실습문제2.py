cnt_list=[]
val_list=[]
new_list=[]

with open('yesterday.txt','r') as f:
    val_list=f.readlines()

for i in val_list:

    temp=(i.strip('\n').split(' '))

    for j in temp:
        new_list.append(j.lower())

val_list=new_list
new_list=list(set(new_list))
new_list.sort(key=str.lower)

new_list.remove('')


print(new_list)

for i in new_list:
    print(f'"{i}":{val_list.count(i)}')
