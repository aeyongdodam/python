m,n=map(int,input().split())
num=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
s=''
if m==0:
    print(0)
else:
    while m>0:
        temp=m%n
        m//=n
        s+=num[temp]
    s=list(s)
    s.reverse()
    print(''.join(s))
