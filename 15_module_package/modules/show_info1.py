def show_name1():
    return print('홍길동')

def show_phone():
    return print("010-1234-1234")


# 모듈로 쓰지않고 이 파일을 메인으로 쓸때만 실행된다!!!!!!!!!!
if __name__ == '__main__':
    print('자신의 모듈 show_info를 호출함')
    show_name1()
    show_phone()