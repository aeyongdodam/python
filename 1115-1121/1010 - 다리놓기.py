import math
n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    ans=math.factorial(m)//math.factorial(n)//math.factorial(m-n)
    print(ans)
#처음에 ans=math.factorial(m)/math.factorial(n)/math.factorial(m-n)
#print(int(ans))했더니 오류남 -> float는 부정확하기 때문(부동소수점)
