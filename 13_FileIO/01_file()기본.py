# 파일 입출력 3단계

# 1단계 : 파일 열기(open)
# 내장함수 open(파일경로, 모드)
# r,w,a, r+,w+, a+ : 텍스트 파일
# rb,wb,ab, rb+,wb+, ab+ : 이진 파일
# +붙은건 그 기능외에 더
# r+는 읽고 쓰기
# w+는 읽고 쓰기(그전 파일 삭제됌)
# a+는 읽고 추가하기

# 2단계 : 파일 처리 => 읽기 / 쓰기
# 파일객체.read()    ,readline(),readlines()
# 파일객체.write()

# 3단계 : 파일 닫기(close)
# 파일객체.close()