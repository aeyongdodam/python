#메모리 초과(부분집합 다 구하는 방법)
import math
li=[]
n=int(input())
num=int(math.log(n,2))
for i in range(num):
    li.append(3**i)
subset=[[]]
for i in li:
    size=len(subset)
    for j in range(size):
        subset.append(subset[j]+[i])
origin=2**num

print(sum(subset[n-origin])+3**(num))
