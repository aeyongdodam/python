n = int(input())
for l in range(n):
    a,b,c=map(str,input().split())
    if len(a)+len(b) != len(c): #a와 b의 문자열 길이를 합친게 문자열 c의 길이와 같지 않으면 not interleaving 출력 후 종료 
        print('Data set '+str(l+1)+': no')
    else:
        dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
        dp[0][0] = 1
        for i in range(1,len(a)+1):
            if a[i-1] == c[i-1]:
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(b)+1):
            if b[i-1] == c[i-1]:
                dp[0][i] = dp[0][i-1]
        for i in range(1,len(a)+1):
            for j in range(1,len(b)+1):
                if a[i-1] == c[i-1+j]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j])
                if b[j-1] == c[i-1+j]:
                    dp[i][j] = max(dp[i][j-1], dp[i][j])
        if dp[-1][-1] == 1:
            print('Data set '+str(l+1)+': yes')
        else:
            print('Data set '+str(l+1)+': no')
