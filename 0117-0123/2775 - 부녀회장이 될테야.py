li=[[0]*14 for i in range(15)]
li[0]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(1,15):
    temp=[]
    num=0
    for j in range(14):
        num+=li[i-1][j]
        temp.append(num)
    li[i]=temp
t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    print(li[k][n-1])
