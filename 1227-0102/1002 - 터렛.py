import math
n=int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    leng=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if (leng==0 and r1==r2):
        print(-1)
    elif leng==0 or (leng+r1)<r2 or (leng+r2)<r1:
        print(0)
    elif (leng==(r1+r2)) or leng+r1==r2 or leng+r2==r1:
        print(1)
    elif leng<(r1+r2):
        print(2)
    else:
        print(0)
