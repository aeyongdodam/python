n=int(input())
temp=[]
final=[]
for i in range(2,1000):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
            
    if flag==True:
        final.append(i)
num=list(map(int,input().split()))
ans=0
for i in num:
    if i in final:
        ans+=1
print(ans)
