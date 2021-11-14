n,m=map(str,input().split())
n= "".join(reversed(n))
m="".join(reversed(m))
ans=int(n)+int(m)
ans="".join(reversed(str(ans)))
k=0
for i in ans:
    if i=='0':
        k+=1
    else:
        break
for i in range(k,len(ans)):
    print(ans[i],end='')
