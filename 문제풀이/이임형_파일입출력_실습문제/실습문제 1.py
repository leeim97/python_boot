f = open('../../13_FileIO/data/s.txt','r')

ob= f.readlines()
# print(ob)

new_list = list()

for i in ob:
    temp=i.rstrip('\n').split(" ")
    # print(temp)
    new_list.append(temp)

new_list.sort()
for i in new_list:
    print(i)