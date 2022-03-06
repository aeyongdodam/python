from itertools import permutations
ans = []
n = int(input())
num = list(map(int,input().split()))
a=list(permutations(num,n))
for i in range(len(a)):
    tmp = 0
    for j in range(n-1):
        tmp+=abs(a[i][j]-a[i][j+1])
    ans.append(tmp)
print(max(ans))
