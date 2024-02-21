num= int(input())
bi=list()
while num >0 :
    bi.append(num%2)
    num//=2

bi.reverse()
print('이진수는 0b',end='')
for i in range(len(bi)):
    print(bi[i],end='')
