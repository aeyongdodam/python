r,c = map(int,input().split())
li = [list(map(int,input().split())) for i in range(c)]
li2 = [list(map(int,input().split())) for i in range(r)]
flag = 1
for i in range(c):
    for j in range(r):
        if li[i][j] != li2[j][c-1-i]:
            flag = 0
            break
if flag ==1:
    print('|>___/|        /}')
    print('| O < |       / }')
    print('(==0==)------/ }')
    print('| ^  _____    |')
    print('|_|_/     ||__|')
else:
    print('|>___/|     /}')
    print('| O O |    / }')
    print('( =0= )""""  \\')
    print('| ^  ____    |')
    print('|_|_/    ||__|')
