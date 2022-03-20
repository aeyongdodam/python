import sys
t=int(sys.stdin.readline())
for i in range(t):
    s1=str(sys.stdin.readline())
    s2=str(sys.stdin.readline())
    ans=0
    j=0
    tmp=0
    while j<len(s1) and j+tmp<len(s2):
        if s1[j]==s2[j+tmp]:
            ans+=1
            j+=1
        else:
            tmp+=1
    if ans==len(s1):
        print("Case #{0}: {1}".format(i+1,len(s2)-len(s1)))
    else:
        print("Case #{0}: IMPOSSIBLE".format(i+1))
        
