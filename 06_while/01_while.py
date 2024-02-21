    #1부터 100사이의 숫자 출력

# i=1
#
# while i<=100:
#     print(i)
#     i+=1

    # 1부터 100 사이 3의 배수들의 합

# total=0
# num=3
# while num<=100:
#     if num%3 ==0:
#         total +=num
#     num+=1
# print('1~100사이의 3의 배수 합',total)

    #7을 입력할때까지 계속 입력하는 프로그램

#num=int(input('숫자 입력 : '))
#while num !=7:
#    num=int(input('다시 입력 : '))

#print(f'{num} 입력! 종료')

# 연습문제 if 1번문제 : 십진수를 이진수로

dec = int(input('십진수입력:'))
bin=''
while dec>0:
    r = dec % 2
    dec=dec//2
    bin= str(r)+bin
print('0b'+bin)