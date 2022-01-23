t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    temp1=n//h+1
    
    temp2=n%h
    if temp2==0:
        temp2=h
        temp1-=1
    floor=str(temp2)
    if temp1<10:
        room='0'+str(temp1)
    else:
        room=str(temp1)
    print(floor+room)
