import sys
import math
M,N = map(int,sys.stdin.readline().split())
num = [0]*(N+1)
num[0] = 1
num[1] = 1
for i in range(2,int(math.sqrt(N))+1):
    if num[i] == 0:
        k=2
        j=i*k
        while(j<=N):
            num[j]=1
            k+=1
            j=i*k
for i in range(M,N+1):
    if num[i]==0:
        print(i)
