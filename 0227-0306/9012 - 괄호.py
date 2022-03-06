n = int(input())
for i in range(n):
    ans = 0
    flag = 1
    s = str(input())
    for j in s:
        if ans<0:
            flag = 0
            break
        if j == '(':
            ans+=1
        elif j == ')':
            ans-=1
    if flag == 1 and ans == 0:
        print("YES")
    else:
        print("NO")
