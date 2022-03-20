import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    s=str(sys.stdin.readline())
    ans=1
    print("Case #{0}:".format(i+1),end="")
    for j in range(len(s)-1):
        print("",ans,end="")
        if s[j]<s[j+1]:
            ans+=1
        else:
            ans=1
        
    print()
