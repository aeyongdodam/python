import sys
def fun(n,s,m,v):
    dp = [[0]*(m+1) for i in range (n+1)]
    dp[0][s]=1
    for i in range(1,n+1):
        for j in range(m+1):
            if dp[i-1][j] == 1:
                if j+v[i-1] <=m:
                    dp[i][j+v[i-1]] = 1
                if j-v[i-1] >= 0:
                    dp[i][j-v[i-1]] = 1
    ans = -1
    for i in range(m+1):
        if dp[n][i] == 1:
            ans = i
    print(ans)
n,s,m = map(int,sys.stdin.readline().split())
v= list(map(int,sys.stdin.readline().split()))
fun(n,s,m,v)
