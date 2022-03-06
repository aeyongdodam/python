a,b=map(str,input().split())
ans=[]
if len(a) > len(b):
    length = len(a)-len(b)
    for i in range(length):
        tmp=len(b)
        for j in range(len(b)):
            if a[i+j] == b[j]:
                tmp-=1
        ans.append(tmp)
else:
    length = len(b)-len(a)
    for i in range(length+1):
        tmp=len(a)
        for j in range(len(a)):
            if a[j] == b[i+j]:
                tmp-=1
        ans.append(tmp)
print(min(ans))
