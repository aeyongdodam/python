t=int(input())
for i in range(t):
    li=[]
    n=int(input())
    li=list(map(int,input().split()))
    ans=[0,0,0,0]
    while(len(li)>2):
        ans=[]
        if len(li)%2==0:
            for j in range((len(li)-1)//2):
                temp=li[j]+li[len(li)-j-1]
                ans.append(temp)
        else:
            for j in range((len(li)-1)//2):
                temp=li[j]+li[len(li)-j-1]
                ans.append(temp)
            ans.append(li[len(li)//2]*2)
            li=[]
            for k in ans:
                li.append(k)
    if li[0]>li[1]:
        name='Alice'
        print("Case #{0}: {1}".format(i+1,name))
    else:
        name='Bob'
        print("Case #{0}: {1}".format(i+1,name))
            
                
