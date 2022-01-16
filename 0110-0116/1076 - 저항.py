color=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
s=''
for i in range(3):
    n=str(input())
    if i<2:
        s+=str(color.index(n))
    else:
        s=int(s)
        temp=10**color.index(n)
        s=s*temp
print(s)
