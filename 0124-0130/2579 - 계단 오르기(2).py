n=int(input())
num=[]
dp=[0]*(n+1)
for i in range(n):
    t=int(input())
    num.append(t)
num.append(0)
if n==1:
    print(num[0])
elif n==2:
    print(num[0]+num[1])
else:
    dp[0]=num[0]
    dp[1]=num[0]+num[1]
    dp[2]=max(num[0]+num[2],num[1]+num[2])
    for i in range(3,n):
        dp[i]=max(dp[i-3]+num[i-1]+num[i],dp[i-2]+num[i])
    print(dp[n-1])
