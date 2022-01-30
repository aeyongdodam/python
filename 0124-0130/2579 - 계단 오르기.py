n=int(input())
num=[]
ans=[]
ans=[[0,0] for i in range(n+1)]
temp=0
for i in range(n):
    t=int(input())
    num.append(t)
num.insert(0,0)
if n==1:
    print(num[1])
elif n==2:
    print(num[1]+num[2])
else:

    for i in range(n+1):
        ans[i][0]=ans[i-1][1]+num[i]
        ans[i][1]=max(ans[i-2])+num[i]
    print(max(ans[n]))
