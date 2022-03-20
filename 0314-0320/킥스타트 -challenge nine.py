import sys
t= int(sys.stdin.readline())
for i in range(t):
    s=str(input())
    n=list(map(int,s))
    a=9-sum(n)%9
    if a==9:
        a=0
    if a==0:
        j=1
    else:
        j=0
    flag=0
    for k in range(j,len(n)):
        if n[k]>a:
            flag=1
            break
    print("Case #{0}: ".format(i+1),end="")
    if flag==1:
        if k>=1:
            print(s[:k],end="")
        print(a,end="")
        print(s[k:])
    else:
        print(s,end="")
        print(a)
