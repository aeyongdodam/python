global flag
def dfs(a,b,c,a_index,b_index,c_index):
    global flag
    if flag == 1:
        return
    if a_index + b_index == len(c)-2:
        flag = 1
        return
    if a_index<=len(a)-1 and a[a_index] == c[c_index]:
        dfs(a,b,c,a_index+1,b_index,c_index+1)
    if b_index<=len(b)-1 and b[b_index] == c[c_index]:
        dfs(a,b,c,a_index,b_index+1,c_index+1)
    return
n = int(input())
for l in range(n):
    semi=1
    a,b,c=map(str,input().split())
    a_alpha=[0]*127
    b_alpha=[0]*127
    c_alpha=[0]*127
    for i in range(len(a)):
        a_alpha[ord(a[i])]+=1
    for i in range(len(b)):
        b_alpha[ord(b[i])]+=1
    for i in range(len(c)):
        c_alpha[ord(c[i])]+=1
    for i in range(len(c_alpha)):
        if a_alpha[i]+b_alpha[i]!=c_alpha[i]:
            semi = 0
            break
    if len(a)+len(b) != len(c): #a와 b의 문자열 길이를 합친게 문자열 c의 길이와 같지 않으면 not interleaving 출력 후 종료 
        print('Data set '+str(l+1)+': no')
    flag = 0
    if semi==1:
        dfs(a,b,c,0,0,0)
    if flag == 1:
        print('Data set '+str(l+1)+': yes')
    else:
        print('Data set '+str(l+1)+': no')
