num=[0]*100
ans=0
n=int(input())
p=list(map(int,input().split()))
for i in p:
    if num[i-1]==1:
        ans+=1
    else:
        num[i-1]=1
print(ans)
