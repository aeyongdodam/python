import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    num =[]
    for j in range(n):
        a,b=map(int,sys.stdin.readline().split())
        num.append([a,b])
    num.sort()
    ans=0
    mini = num[0][1]
    for j in range(n):
        if mini>=num[j][1]:
            mini = num[j][1]
            ans+=1
    print(ans)
