import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    s=str(sys.stdin.readline())
    k='0'*n
    k=k+s
    k=k+'0'*n
    ans = 0
    for j in range(n,2*n):
        tmp=0

        while True:
            a=k[j+tmp]
            b=k[j-tmp]
            if k[j+tmp]=='1' or k[j-tmp]=='1':
                ans+=tmp
                break
            else:
                tmp+=1
    print("Case #{0}: {1}".format(i+1,ans))
