# main

name=''
def input_name():
    global name
    name = input('이름입력:')

def get_name():
    if name == '':
        return 'noname'
    else:
        return name

if __name__ == '__main__':
    input_name()
    print(get_name())