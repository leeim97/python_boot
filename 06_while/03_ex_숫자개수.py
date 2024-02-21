p_cnt=0
m_cnt=0
z_cnt=0

for i in range(10):
    num=int(input(f'숫자 {i+1}입력 : '))
    if num >0:
        p_cnt+=1
    elif num <0:
        m_cnt +=1
    else:
        z_cnt+=1
print('---------------------')
print(f'양의 개수 : {p_cnt}')
print(f'음의 개수 : {m_cnt}')
print(f'0의 개수 : {z_cnt}')