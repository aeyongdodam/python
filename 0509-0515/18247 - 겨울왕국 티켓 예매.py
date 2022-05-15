n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a < 12 or b < 4:
        print(-1)
    else:
        print(11*b+4)
