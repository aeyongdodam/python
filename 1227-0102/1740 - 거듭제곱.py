n=int(input())
num=[]
total=0
while n>0:
    num.append(n%2)
    n//=2
temp=0
for i in num:    
    total+=3**temp*i
    temp+=1
print(total)
