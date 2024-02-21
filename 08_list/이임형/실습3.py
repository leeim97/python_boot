
ch="23"
ls=list()
while ch != '':
    ch= input("상품 등록 (엔터키를 누르면 종료) : ")
    #print(ch)
    ls.append(ch)

ls.pop()
print(f'등록된 상품 : {ls}')