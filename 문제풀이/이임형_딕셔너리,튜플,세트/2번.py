d=dict()

while True:
    name=input('영어 단어 등록 (종료는 quit) : ')
    if name == 'quit':
        break

    if name not in d.keys():
        mean = input(f'{name}뜻 입력 (종료는 quit) : ')
        if name == 'quit':
            break

        d[name]=mean

    else:
        print(f'{name}은 이미 등록된 단어 입니다.')

while True:
    name=input('검색할 단어 입력 (종료는 quit) : ')

    if name == 'quit':
        print('종료합니다.')
        break

    mean=d.get(name)
    if mean == None:
        print(f'{name}은 사전에 없는 단어 입니다.')
    else :
        print(f'{name}의 뜻은 {mean}입니다')