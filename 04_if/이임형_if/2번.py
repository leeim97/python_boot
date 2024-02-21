num= input()

if 'a'<=num and num<='f':
    print(ord(num)-ord('a')+10)
elif 'A'<=num and num<='F':
    print(ord(num)-ord('A')+10)
elif '0'<=num and num<='9':
    print(ord(num)-ord('0'))
else:
    print('16진수가 아닙니다')
