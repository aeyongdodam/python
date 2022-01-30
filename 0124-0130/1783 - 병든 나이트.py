#그리디 
n,m=map(int,input().split())
if n==1:
    print(1)
elif n==2:
    if m%2==0:
        ans=m//2
    else:
        ans=m//2+1
    if ans>=4:
        print(4)
    else:
        print(ans)
else:
    if m<7:
        print(min(4,m))
    else:
        print(m-6+4)
