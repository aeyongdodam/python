global ans
ans = 0
def dfs(n, i):
    global ans
    if n==0:
        ans+=1
        return
    if (n > 0):
        if i==0:
            dfs(n-1, i+1)
        elif i==9:
            dfs(n-1, i-1)
        else:
            dfs(n-1, i-1)
            dfs(n-1, i+1)
            
n = int(input())

for i in range(1,10):
    dfs(n-1, i)
print(ans % 1000000000)
