num=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n,b=map(str,input().split())
b=int(b)
k=0
ans=0
n=''.join(reversed(n))
for i in n:
    temp=(b**k)*num.index(i)
    ans+=temp
    k+=1
print(ans)
