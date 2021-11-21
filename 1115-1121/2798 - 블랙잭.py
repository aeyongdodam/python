n,m=map(int,input().split())
num=list(map(int,input().split()))
ans=0
for i in range(0,len(num)-2):
    for j in range(i+1,len(num)-1):
        for k in range(j+1,len(num)):
            if num[i]+num[j]+num[k]>m:
                continue
            else:
                ans=max(ans,num[i]+num[j]+num[k])
print(ans)
