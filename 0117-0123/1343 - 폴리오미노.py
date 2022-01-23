s=str(input())
num_x=0
ans=''
flag=True
for i in s:
    if i=='X':
       num_x+=1
    else:
        if num_x==0:
            ans+='.'
            continue
        elif num_x%2==1:
            flag=False
            break
        else:
            A_num=num_x//4
            num_x=num_x%4
            B_num=num_x//2
            ans=ans+'AAAA'*A_num+'BB'*B_num
        ans+='.'
        num_x=0
if num_x%2==1:
    flag=False
else:
    A_num=num_x//4
    num_x=num_x%4
    B_num=num_x//2
    ans=ans+'AAAA'*A_num+'BB'*B_num
if flag==True:
    print(ans)
else:
    print(-1)
            
