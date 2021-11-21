    n,m=map(int,input().split())
    li=[]
    for i in range(n):
        num=str(input())
        li.append(num)
    row=[0]*n
    column=[0]*m
    for i in range(n):
        temp=li[i]
        for j in range(m): 
            if temp[j]=='X':
                row[i]=1
                column[j]=1
    r=n-row.count(1)
    c=m-column.count(1)
    print(max(r,c))
