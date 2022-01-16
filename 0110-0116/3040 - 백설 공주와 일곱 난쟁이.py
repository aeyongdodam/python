li=[]
for i in range(9):
    n=int(input())
    li.append(n)
for i in range(8):
    for j in range(i+1,9):
        ans=0
        for k in range(9):
            if k==i or k==j:
                continue
            else:
                ans+=li[k]
        if ans==100:
            for k in range(9):
                if k==i or k==j:
                    continue
                print(li[k])
                
    
