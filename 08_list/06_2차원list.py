# 2차원 리스트 : [행][열]

table=[[1,2,3,4],[7,8,9,10],[10,11,12,14]]
print(table)
print(len(table))

#이중리스트 for 문은 행 한줄씩 나오네
for row in table:
    print(row,type(row),len(row))

for row in table:
    for column in row:
        print(column,end=" ")
    print('')

row_n=len(table)
col_n=len(table[0])

for r in range(row_n):
    for c in range(col_n):
        print(table[r][c],end=" ")
    print("")