import sys
ans = [0]*(123456*2)
i = 2
while (i*i<=2*123456):
    for j in range(2*123456):
        if j % i == 0 and j != i:
            ans[j] = 1
    i+=1
n = -1
while (1):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        ret = 0
        for i in range(n+1,2*n):
            if ans[i] == 0:
                ret+=1
        print(ret)
    
