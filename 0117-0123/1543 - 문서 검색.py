s=str(input())
find=str(input())
l=len(find)
ans=0
while True:
    if find in s:
        ans+=1
        index_find=s.index(find)+l
        s=s[index_find:]
    else:
        break
print(ans)
