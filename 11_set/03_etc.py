# zip() 함수

foods=['떡볶이','짜장면','피자','라면']
sides =['김치','단무지','피클']

zipObj = zip(foods,sides)
zip_list= list(zipObj)
zip_dict= dict(zip(foods,sides))
print(zip_list)
print(zip_dict)

# 리스트 컴프리핸션

xlist=[x*2 for x in range(1,11) ]
print(xlist)

ylist=[x+y for x in range(1,11) for y in range(10,21) ]
print(ylist)

foodList=[(x,y) for x in ['밥','국주','짜장면'] for y in ['김치','단무지']]
print(foodList)

# 세트 컴프리핸션
ySet={x+y for x in range(1,5)  for y in range(2,6)}
print(ySet)

# 딕셔너리 컴프리핸션 같은 키값은 맨 마지막 value니까 피클만 남음
print( {food:side for food in foods for side in sides})
#{'떡볶이': '피클', '짜장면': '피클', '피자': '피클', '라면': '피클'}

stds= ['철수','영희','길동','순희']
std_dic = {s:0 for s in stds}
print(std_dic)
print(std_dic.items())

stds= {'철수':90,'영희':50,'길동':60,'순희':100}
std_scores={ name:'pass' if score > 60 else 'non-pass' for name ,score in stds.items() }
print(std_scores)