import sys
t=int(sys.stdin.readline())
for i in range(t):
    n,k=map(int,sys.stdin.readline().split())
    s=str(sys.stdin.readline())
    ans=0
    for j in range(n//2):
        if s[j]!=s[n-j-1]:
            ans+=1
    print("Case #{0}: {1}".format(i+1,abs(ans-k)))
