pan=[[0 for i in range(100)]for j in range(100)]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    for a in range(10):
        for b in range(10):
            pan[x+a][y+b]=1
    ans=0
    for m in pan:
        ans+=sum(m)
print(ans)
