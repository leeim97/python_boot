from random import randint
k=["개과천선","구사일생","군계일학","무용지물","동고동락","유비무환","입신양명","괄목상대","막역지우","고장난명"]
m=["개과천선뜻","구사일생뜻","군계일학뜻","무용지물뜻","동고동락뜻","유비무환뜻","입신양명뜻","괄목상대뜻","막역지우뜻","고장난명뜻"]

print("사자성어 맞추기 게임을 시작합니다")
print("-------------------------------")

while True:
    num=randint(0,9)
    value=m[num]
    print(value)
    mean=input()
    if mean == k[num] :
        print('맞습니다.. 게임을 종료합니다.')
        break
    else:
        print("다시!")

#ddd