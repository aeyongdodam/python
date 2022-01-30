n=int(input())
num=list(map(int,input().split()))
ans=[]
for i in range(n):
    ans.append(num[i])
for i in range(1,n):
    for j in range(i):
        if num[i]>num[j]:
            ans[i]=max(ans[j]+num[i],ans[i])
print(max(ans))
