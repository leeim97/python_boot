# binary file: 이진 파일
# - 글자(text)가 아닌 bit 단위로 의미가 부여되는파일
# - 텍스트파일을 제외한 파일 : 그림파일, 음악파일, 동영상파일, 엑셀, 실행exe
# - 텍스트파일과 이진 파일 구분 : 메모장에서 파일 열기 시 내용이 보이면 텍스트 ,이상하게 보이면 이진

instr=''

path1= 'c:/Windows/notepad.exe'
path2='data/notepad.exe'

inF = open(path1,'rb')
outF=open(path2,'wb')

while True:
    instr = inF.read(1) #1 바이트씩 읽기
    if not instr:
        break
    outF.write(instr)

inF.close()
outF.close()