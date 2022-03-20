import sys
def di(n):
    ans=1
    while n>0:
        ans*=n%10
        n//=10
    return ans
def su(n):
    ans=0
    while n>0:
        ans+=n%10
        n//=10
    return ans
t=int(sys.stdin.readline())
for j in range(t):
    a,b=map(int,sys.stdin.readline().split())
    ans=0
    for i in range(a,b+1):
        d=di(i)
        s=su(i)
        if d%s==0:
            ans+=1
    print("Case #{0}: ".format(j+1),end="")
    print(ans)
