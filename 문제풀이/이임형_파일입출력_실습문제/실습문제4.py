def input_member(path):
    with open(path,'w',encoding='utf-8') as f:

        while True:
            temp=(input('멤버를 입력하세요.(종료는 q) : '))
            if temp=='q':
                return
            else:
                f.write(temp+'\n')

def output_member(save):
    with open(save,'r',encoding='utf-8') as f:
        print(f.read(),end="")


while True:
    ch=input('저장 1, 출력 2, 종료 q : ')
    if ch == '1':
        path=input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(path)
    elif ch == '2':
        save=input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(save)
    elif ch== 'q':
        break
