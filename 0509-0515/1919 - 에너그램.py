a = str(input())
b = str(input())
alpha_a = [0]*26
alpha_b = [0]*26
for i in a:
    alpha_a[ord(i)-97] +=1
for i in b:
    alpha_b[ord(i)-97] +=1
ans = 0
for i in range(len(alpha_a)):
    ans += abs(alpha_a[i] - alpha_b[i])
print(ans)
