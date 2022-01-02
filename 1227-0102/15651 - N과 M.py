n,m=map(int,input().split())
subset=[[]]
for k in range(m):
    for j in range(len(subset)):
        for i in range(1,n+1):
            subset.append(subset[j]+[i])
for i in range(len(subset)):
    if len(subset[i])==m:
        for j in range(m):
            print(subset[i][j],end=" ")

        print("")
        
