f=str(input())
n=int(input())
new=''
for i in range(len(f)-2):
    new+=f[i]
new+='00'
new=int(new)
final=new%n
if final==0:
    new=str(new)
    print(new[len(new)-2]+new[len(new)-1])
else:
    new=new+n-final
    new=str(new)
    print(new[len(new)-2]+new[len(new)-1])
