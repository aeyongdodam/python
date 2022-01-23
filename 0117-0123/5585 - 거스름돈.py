n=int(input())
n=1000-n
money=[500,100,50,10,5,1]
ans=0
for i in money:
    temp=n//i
    n-=temp*i
    ans+=temp
print(ans)
