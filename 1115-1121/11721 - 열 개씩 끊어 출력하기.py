s=input()
k=0
for i in s:
    if k==10:
        print("")
        print(i,end="")
        k=1
    else:
        print(i,end="")
        k+=1
