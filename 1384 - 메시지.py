n=-1
it=1
while(True):
    flag=False
    num=[]
    n=int(input())
    if n==0:
        break
    else:
        if it>=2:
            print("")
        num=[list(map(str,input().split())) for j in range(n)]
        print('Group',it)
        for i in range(n):
            for j in range(1,len(num[i])):
                if num[i][j]=='N':
                    flag=True
                    temp=(i-j+n)%n
                    nameA=num[temp][0]
                    nameB=num[i][0]
                    print(nameA,"was nasty about",nameB)
        if flag==False:
            print('Nobody was nasty')
        it+=1
                    
    
