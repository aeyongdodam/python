factorial =[1,2,6,24,120]
while(1):
    n=int(input())
    if n == 0:
        break
    ans = 0
    i = 0
    while i<=4:
        tmp = n%10
        ans += tmp * factorial[i]
        n = n//10
        i+=1
    print(ans)
