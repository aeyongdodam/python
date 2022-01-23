n=int(input())
divisor=[]
temp=0
k=0
for i in range(2,n+1):
    if n==0:
        break
    while n%i==0:
        divisor.append(i)
        n//=i
while 2**k<len(divisor):
    temp+=1
    k+=1
print(temp)
