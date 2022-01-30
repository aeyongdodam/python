fibo=[[1,0],[0,1]]
for i in range(2,41):
    temp1=fibo[i-1][0]+fibo[i-2][0]
    temp2=fibo[i-1][1]+fibo[i-2][1]
    fibo.append([temp1,temp2])
t=int(input())
for i in range(t):
    n=int(input())
    print(fibo[n][0],fibo[n][1])
