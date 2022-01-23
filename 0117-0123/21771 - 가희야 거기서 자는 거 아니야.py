r,c=map(int,input().split())
rg,cg,rp,cp=map(int,input().split())
flag=False
li=[]
for k in range(r):
    temp=str(input())
    li.append(temp)
for i in range(r):
    if 'G' in li[i] and 'P' in li[i]:
        flag=True
        break
if flag==True:
    print(1)
else:
    print(0)
