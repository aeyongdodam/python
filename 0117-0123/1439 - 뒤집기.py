s=str(input())
li=[0,0]
temp1=int(s[0])
li[temp1]+=1
for i in s:
    if temp1!=int(i):
        temp1=int(i)
        li[temp1]+=1
print(min(li))
