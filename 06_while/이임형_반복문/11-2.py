for i in range(5,0,-1):
    for j in range(0,i-1):
        print(' ',end='')
    for k in range(9-2*(i-1)):
        print('*',end='')
    for j in range(0,i-1):
        print(' ',end='')
    print('')