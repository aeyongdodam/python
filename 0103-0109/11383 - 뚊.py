n,m=map(int,input().split())
string=[]
answer=[]
flag=True
for i in range(n):
    a=str(input())
    string.append(a)
for j in range(n):
    a=str(input())
    answer.append(a)
for i in range(n):
    ans=''
    for j in string[i]:
        ans+=j*2
    if ans==answer[i]:
        continue
    else:
        flag=False
        break
if flag==True:
    print('Eyfa')
else:
    print('Not Eyfa')
