path='../../13_FileIO/data/number.txt'
save='../../13_FileIO/data/number++.txt'
def my_sum(path,save):
    t_list = []
    with open(path, 'r') as f:
        while True:

            temp = f.readline()
            if not temp:
                break

            t_list.append(temp.strip('\n'))

    for i in t_list:
        if i == '':
            t_list.remove(i)

    print(t_list)

    cnt=[]
    for i in t_list:
        num1,num2=map(int,i.split())
        cnt.append(f'{num1}+{num2}={num1+num2:.1f}')

    print(cnt)

    with open(save,'w') as f:
        for i in cnt:
          f.write(i+'\n')

my_sum(path,save)

